import numpy as np
import scipy.optimize as spopt

import dieta.foods as dif

starch = dif.FoodsById[2]
veggie = dif.FoodsById[21]
meatie = dif.FoodsById[5]
otherf = dif.FoodsById[7]

# A meal has:
# Target number of cals: T_cal
# Target weights of fats, carbs, and protein: P_all = [P_fat, P_crb, P_pro], where sum(P_all) == 1
# One or more foods: [F_0, F_1, ..., F_n]
# Each food has a per-unit quantity of fat, carb, and protein: F_0_f, F_0_c, F_0_p, F_1_f, F_1_c, F_1_p,
#     ..., F_n_f, F_n_c, F_n_p
# We want to find the quantities of each food q_0, q_1, ..., q_n such that:
#     F_0_f * 9 * q_0 + F_0_c * 4 * q_0 + F_0_p * 4 * q_0
#   + F_1_f * 9 * q_1 + F_1_c * 4 * q_1 + F_1_p * 4 * q_1
#   + ...
#   + F_n_f * 9 * q_n + F_n_c * 4 * q_n + F_n_p * 4 * q_n = T_cal

# Alternatively:
#     F_0_f * 9 * q_0 + F_1_f * 9 * q_1 + ... + F_n_f * 9 * q_n = T_cal * P_fat
#     F_0_c * 9 * q_0 + F_1_c * 9 * q_1 + ... + F_n_c * 9 * q_n = T_cal * P_crb
#     F_0_p * 9 * q_0 + F_1_p * 9 * q_1 + ... + F_n_p * 9 * q_n = T_cal * P_pro

target_ratios = np.array([25, 45, 30])
norm = np.sum(target_ratios)
target_ratios = target_ratios / norm

target_cals = 300

target_cals_per_macro = target_cals * target_ratios

print(f'Target Cals/Macro: {target_cals_per_macro}')

if __name__ == '__main__':
    unit_cals_from_fat = []
    unit_cals_from_crb = []
    unit_cals_from_pro = []
    for food in (meatie, veggie, starch, otherf):
        unit_food = food.per_unit()
        unit_macros = unit_food.macros()

        print(f'Food Name: {food.name}')
        print(f'Unit Cals from Fat: {unit_macros.fat_cals()}')
        print(f'Unit Cals from Carbs: {unit_macros.crb_cals()}')
        print(f'Unit Cals from Protein: {unit_macros.pro_cals()}')

        unit_cals_from_fat.append(unit_macros.fat_cals())
        unit_cals_from_crb.append(unit_macros.crb_cals())
        unit_cals_from_pro.append(unit_macros.pro_cals())

    # print(unit_cals_from_fat)
    # print(unit_cals_from_crb)
    # print(unit_cals_from_pro)

    a = np.array([unit_cals_from_fat, unit_cals_from_crb, unit_cals_from_pro])
    # print(a)
    b = target_cals_per_macro
    print(f'Units of Each Food to Consume: {spopt.nnls(a, b)[0]}')

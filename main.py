import dieta.foods

if __name__ == '__main__':
    for d in dieta.foods.FoodDefs:
        print(d)
        print(d.per_unit().macros().total_cals())

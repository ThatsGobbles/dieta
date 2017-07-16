import typing as typ
import enum


class MacrosDef(typ.NamedTuple):
    g_fat: float
    g_crb: float
    g_pro: float

    def fat_cals(self) -> float:
        return self.g_fat * 9

    def crb_cals(self) -> float:
        return self.g_crb * 4

    def pro_cals(self) -> float:
        return self.g_pro * 4

    def total_cals(self):
        return self.pro_cals() + self.crb_cals() + self.fat_cals()

    def pct_from_fat(self):
        return self.fat_cals() / self.total_cals()

    def pct_from_crb(self):
        return self.crb_cals() / self.total_cals()

    def pct_from_pro(self):
        return self.pro_cals() / self.total_cals()


class Units(enum.Enum):
    G = enum.auto()
    ML = enum.auto()


class FoodDef(typ.NamedTuple):
    id: int
    name: str
    sample_qty: float
    sample_units: Units
    g_fat: float
    g_crb: float
    g_pro: float
    modifiers: typ.Sequence[str] = ()

    def scale(self, factor: float) -> 'FoodDef':
        new_sample_qty = self.sample_qty * factor
        new_g_fat = self.g_fat * factor
        new_g_crb = self.g_crb * factor
        new_g_pro = self.g_pro * factor
        return self._replace(sample_qty=new_sample_qty, g_fat=new_g_fat, g_crb=new_g_crb, g_pro=new_g_pro)

    def scale_to(self, new_qty: float) -> 'FoodDef':
        factor = new_qty / self.sample_qty
        return self.scale(factor)

    def per_unit(self) -> 'FoodDef':
        return self.scale_to(1)

    def macros(self) -> MacrosDef:
        return MacrosDef(g_fat=self.g_fat, g_crb=self.g_crb, g_pro=self.g_pro)

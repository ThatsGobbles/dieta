import typing as typ
import enum


class MacrosDef(typ.NamedTuple):
    g_prot: float
    g_fats: float
    g_carb: float

    def scale(self, factor: float) -> 'MacrosDef':
        new_g_prot = self.g_prot * factor
        new_g_fats = self.g_fats * factor
        new_g_carb = self.g_carb * factor
        return self._replace(g_prot=new_g_prot, g_fats=new_g_fats, g_carb=new_g_carb)


class Units(enum.Enum):
    G = enum.auto()
    ML = enum.auto()


class FoodDef(typ.NamedTuple):
    name: str
    sample_qty: float
    sample_units: Units
    g_prot: float
    g_fats: float
    g_carb: float

    def scale(self, factor: float) -> 'FoodDef':
        new_sample_qty = self.sample_qty * factor
        new_g_prot = self.g_prot * factor
        new_g_fats = self.g_fats * factor
        new_g_carb = self.g_carb * factor
        return self._replace(sample_qty=new_sample_qty, g_prot=new_g_prot, g_fats=new_g_fats, g_carb=new_g_carb)

    def scale_to(self, new_qty: float) -> 'FoodDef':
        factor = new_qty / self.sample_qty
        return self.scale(factor)

    def per_unit(self) -> 'FoodDef':
        return self.scale_to(1)

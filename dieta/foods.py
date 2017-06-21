from .defs import FoodDef, Units

FoodDefs = (
    FoodDef(name='sweet potatoes'
            , sample_qty=100
            , sample_units=Units.G
            , g_fats=0
            , g_carb=21
            , g_prot=2
            ),
    FoodDef(name='brown rice'
            , sample_qty=2780
            , sample_units=Units.G
            , g_fats=32.9
            , g_carb=869
            , g_prot=89.3
            ),
    FoodDef(name='quinoa'
            , sample_qty=3030
            , sample_units=Units.G
            , g_fats=51.4
            , g_carb=542.8
            , g_prot=119.5
            ),
)

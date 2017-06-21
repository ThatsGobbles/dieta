from .defs import FoodDef, Units

FoodDefs = (
    FoodDef(name='sweet potatoes'
            , sample_qty=100
            , sample_units=Units.G
            , g_fat=0
            , g_crb=21
            , g_pro=2
            ),
    FoodDef(name='brown rice'
            , sample_qty=2780
            , sample_units=Units.G
            , g_fat=32.9
            , g_crb=869
            , g_pro=89.3
            ),
    FoodDef(name='quinoa'
            , sample_qty=3030
            , sample_units=Units.G
            , g_fat=51.4
            , g_crb=542.8
            , g_pro=119.5
            ),
    FoodDef(name='ground beef'
            , modifiers=('90%',)
            , sample_qty=154
            , sample_units=Units.G
            , g_fat=19
            , g_crb=0
            , g_pro=44
            ),
    FoodDef(name='ground beef'
            , modifiers=('96%',)
            , sample_qty=2100
            , sample_units=Units.G
            , g_fat=90
            , g_crb=0
            , g_pro=480
            ),
    FoodDef(name='ground chicken'
            , modifiers=('95%',)
            , sample_qty=1000
            , sample_units=Units.G
            , g_fat=44
            , g_crb=0
            , g_pro=203
            ),
    FoodDef(name='milk'
            , modifiers=('whole',)
            , sample_qty=100
            , sample_units=Units.ML
            , g_fat=3.3
            , g_crb=5.4
            , g_pro=3.3
            ),
    FoodDef(name='milk'
            , modifiers=('2%',)
            , sample_qty=100
            , sample_units=Units.ML
            , g_fat=2
            , g_crb=5.2
            , g_pro=3.4
            ),
    FoodDef(name='milk'
            , modifiers=('1%',)
            , sample_qty=100
            , sample_units=Units.ML
            , g_fat=1
            , g_crb=5.1
            , g_pro=3.6
            ),
    FoodDef(name='milk'
            , modifiers=('skim',)
            , sample_qty=100
            , sample_units=Units.ML
            , g_fat=0.3
            , g_crb=5.2
            , g_pro=3.7
            ),
    FoodDef(name='protein powder'
            , modifiers=('Isopure', 'unflavored')
            , sample_qty=29
            , sample_units=Units.G
            , g_fat=0
            , g_crb=0
            , g_pro=26
            ),
    FoodDef(name='rolled oats'
            , modifiers=('raw',)
            , sample_qty=200
            , sample_units=Units.G
            , g_fat=14.6
            , g_crb=133.3
            , g_pro=29.2
            ),
    FoodDef(name='blueberries'
            , modifiers=('raw',)
            , sample_qty=100
            , sample_units=Units.G
            , g_fat=0.3
            , g_crb=14.5
            , g_pro=0.7
            ),
    FoodDef(name='blueberries'
            , modifiers=('dried', 'unsweetened')
            , sample_qty=100
            , sample_units=Units.G
            , g_fat=0
            , g_crb=82.5
            , g_pro=2.5
            ),
    FoodDef(name='banana'
            , modifiers=('raw',)
            , sample_qty=100
            , sample_units=Units.G
            , g_fat=0.3
            , g_crb=22.8
            , g_pro=1.1
            ),
    FoodDef(name='almond milk'
            , modifiers=('Calafia Farms', 'unsweetened',)
            , sample_qty=200
            , sample_units=Units.ML
            , g_fat=2.5
            , g_crb=0.8
            , g_pro=0.8
            ),
    FoodDef(name='egg'
            , modifiers=('large', 'whole', 'raw',)
            , sample_qty=51
            , sample_units=Units.G
            , g_fat=4.8
            , g_crb=0.4
            , g_pro=6.3
            ),
    FoodDef(name='egg'
            , modifiers=('large', 'white only', 'raw',)
            , sample_qty=34
            , sample_units=Units.G
            , g_fat=0.1
            , g_crb=0.2
            , g_pro=3.6
            ),
    FoodDef(name='powdered milk'
            , modifiers=('skim',)
            , sample_qty=100
            , sample_units=Units.G
            , g_fat=0.8
            , g_crb=52
            , g_pro=32.6
            ),
    FoodDef(name='olive oil'
            , sample_qty=100
            , sample_units=Units.ML
            , g_fat=91.2
            , g_crb=0
            , g_pro=0
            ),
)

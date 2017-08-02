from .model import *
from .necron_weapons import *

annihilation_barge_gauss = Model(name='Barge/Gauss', ballistic=3, weapons=[TeslaDestructor(), TeslaDestructor(), GaussCannon()], base_cost=133)
annihilation_barge_tesla = Model(name='Barge/Tesla', ballistic=3, weapons=[TeslaDestructor(), TeslaDestructor(), TeslaCannon()], base_cost=133)
destroyer = Model(name='Destroyer', ballistic=2.33, weapons=[GaussCannon()], base_cost=43)
blade_gauss = Model(name='Tomb Blade/Gauss', ballistic=3, weapons=[GaussBlaster(), GaussBlaster()], base_cost=24)
blade_tesla = Model(name='Tomb Blade/Tesla', ballistic=3, weapons=[TeslaCarbine(), TeslaCarbine()], base_cost=24)
blade_particle = Model(name='Tomb Blade/Particle', ballistic=3, weapons=[ParticleBeamer()], base_cost=24)
doom_scythe = Model(name='Doom Scythe', ballistic=3, weapons=[DeathRay(), TeslaDestructor(), TeslaDestructor()], base_cost=220)
night_scythe = Model(name='Night Scythe', ballistic=3, weapons=[TeslaDestructor(), TeslaDestructor()], base_cost=174)
warrior = Model(name='Warrior', ballistic=3, weapons=[GaussFlayer()], base_cost=12)
immortal_gauss = Model(name='Immortal/Gauss', ballistic=3, weapons=[GaussBlaster()], base_cost=8)
immortal_tesla = Model(name='Immortal/Tesla', ballistic=3, weapons=[TeslaCarbine()], base_cost=8)
tesseract_vault = Model(name='Tesseract Vault', ballistic=3, weapons=[TeslaSphere(), TeslaSphere(), TeslaSphere(), TeslaSphere()], base_cost=496)

stalker_gauss = Model(name='Stalker/Gauss', ballistic=3, weapons=[TwinHeavyGaussCannon()], base_cost=117)
stalker_particle = Model(name='Stalker/particle', ballistic=3, weapons=[ParticleShredder()], base_cost=117)

heavy_destroyer = Model(name='Heavy destroyer', ballistic=2.33, weapons=[HeavyGaussCannon()], base_cost=43)

necron_models_list = [
    warrior,
    immortal_gauss,
    immortal_tesla,
    blade_gauss,
    blade_tesla,
    blade_particle,
    destroyer,
    annihilation_barge_gauss,
    annihilation_barge_tesla,
    stalker_gauss,
    stalker_particle,
    heavy_destroyer,
    night_scythe,
    doom_scythe,
    tesseract_vault
]
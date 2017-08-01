from .weapon import *

bio_plasmic_cannon = Weapon(name='Bio-Plasmic cannon', point_cost=66,
                            profiles=[Profile(min_range=0, max_range=36, strength=7, ap=3, shots=6, damage=2)])
bio_plasmic_cannon_stationary = Weapon(name='Bio-Plasmic cannon stationary', point_cost=66,
                                       profiles=[Profile(min_range=0, max_range=36, strength=7, ap=3, shots=12, damage=2)])

deathspitter_moster = Weapon(name='Deathspitter (monster)', point_cost=10,
                             profiles=[Profile(min_range=0, max_range=18, strength=7, ap=1, shots=3, damage=1)])

devourer_moster = Weapon(name='Devourer (monster)', point_cost=7,
                             profiles=[Profile(min_range=0, max_range=18, strength=6, ap=0, shots=3, damage=1)])

fleshborer = Weapon(name='fleshborer', point_cost=0,
                            profiles=[Profile(min_range=0, max_range=12, strength=4, ap=0, shots=1, damage=1)])

heavy_venom_cannon = Weapon(name='hvy VC', point_cost=30,
                            profiles=[Profile(min_range=0, max_range=36, strength=9, ap=1, shots=2, damage=2)])

impaler_cannon = Weapon(name='impaler cannon', point_cost=30,
                            profiles=[Profile(min_range=0, max_range=36, strength=8, ap=2, shots=2, damage=2)])
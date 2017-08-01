from .model import *
from .tyranid_weapons import *

tyrant_devourers = Model(name='tyrant/devourers', ballistic=3, weapons=[devourer_moster, devourer_moster, devourer_moster, devourer_moster], base_cost=144+27)
tyrant_deathspitters = Model(name='tyrant/deathspitters', ballistic=3, weapons=[deathspitter_moster, deathspitter_moster, deathspitter_moster, deathspitter_moster], base_cost=144+27)

gaunt_fleshborer = Model(name='gaunt/fleshborer', ballistic=4, weapons=[fleshborer], base_cost=4)

hive_guard = Model(name='hive guard', ballistic=3, weapons=[impaler_cannon], base_cost=18)

harpy = Model(name='harpy', ballistic=4, weapons=[heavy_venom_cannon, heavy_venom_cannon], base_cost=91)

carnifex_devourers = Model(name='carnifex/devourers', ballistic=4, weapons=[devourer_moster, devourer_moster, devourer_moster, devourer_moster], base_cost=74)
carnifex_deathspitters = Model(name='carnifex/deathspitters', ballistic=4, weapons=[deathspitter_moster, deathspitter_moster, deathspitter_moster, deathspitter_moster], base_cost=74)

exocrine_stationary = Model(name='exocrine stationary', ballistic=3, weapons=[bio_plasmic_cannon_stationary], base_cost=162)


tyranid_models_list = [
    gaunt_fleshborer,
    tyrant_devourers,
    tyrant_deathspitters,
    hive_guard,
    harpy,
    carnifex_devourers,
    carnifex_deathspitters,
    exocrine_stationary
]
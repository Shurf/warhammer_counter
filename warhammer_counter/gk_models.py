from .model import *
from .gk_weapons import *

dreadknight = Model(name='Dreadknight w/teleporter', ballistic=3, weapons=[HeavyPsycannon(), HeavyIncinerator()], base_cost=140)

gk_models_list = [
    dreadknight
]
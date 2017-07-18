from .weapon import *

class HeavyPsycannon(Weapon):
    def __init__(self):
        super().__init__('Heavy Psycannon',
                         30,
                         [Profile(min_range=0, max_range=24, strength=7, shots=6, ap=1, damage=2)])


class HeavyIncinerator(Weapon):

    def is_autohit(self):
        return True
    def __init__(self):
        super().__init__('Heavy Incinerator',
                         40,
                         [Profile(min_range=0, max_range=12, strength=6, shots=3.5, ap=1, damage=2)])
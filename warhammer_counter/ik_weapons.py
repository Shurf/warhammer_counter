from .weapon import *

class AvengerGatlingCannon(Weapon):
    def __init__(self):
        super().__init__('avenger gatling cannon',
                         95,
                         [Profile(min_range=0, max_range=36, strength=6, shots=12, ap=2, damage=2)])

class HeavyFlamer(Weapon):
    def is_autohit(self):
        return True
    def __init__(self):
        super().__init__('heavy flamer',
                         17,
                         [Profile(min_range=0, max_range=8, strength=5, shots=3.5, ap=1, damage=1)])


class HeavyStubber(Weapon):
    def __init__(self):
        super().__init__('heavy stubber',
                         4,
                         [Profile(min_range=0, max_range=36, strength=4, shots=3, ap=0, damage=1)])


class MeltaGun(Weapon):
    def __init__(self):
        super().__init__('meltagun',
                         17,
                         [Profile(min_range=6, max_range=12, strength=8, shots=1, ap=4, damage=3.5),
                          Profile(min_range=0, max_range=6, strength=8, shots=1, ap=4, damage=4.47)])


class IronstormMissilePod(Weapon):
    def __init__(self):
        super().__init__('ironstorm missile pod',
                         16,
                         [Profile(min_range=0, max_range=72, strength=5, shots=3.5, ap=1, damage=2)])

class StormspearRocketPod(Weapon):
    def __init__(self):
        super().__init__('stormspear rocket pod',
                         45,
                         [Profile(min_range=0, max_range=48, strength=8, shots=3, ap=2, damage=3.5)])

class ThermalCannon(Weapon):
    def __init__(self):
        super().__init__('thermal cannon',
                         76,
                         [Profile(min_range=0, max_range=18, strength=9, shots=2, ap=4, damage=3.5),
                          Profile(min_range=18, max_range=36, strength=9, shots=2, ap=4, damage=4.47)])

class RapidFireBattleCannon(Weapon):
    def __init__(self):
        super().__init__('Rapid fire battle Cannon',
                         100,
                         [Profile(min_range=0, max_range=72, strength=8, shots=7, ap=2, damage=2)])
from .weapon import *

class SplinterWeapon(Weapon):
    def __init__(self, name: str, point_cost: int, profiles: typing.List[Profile]):
        super().__init__(name=name, point_cost=point_cost, profiles=profiles)

    def wound_probability(self, range_value: int, target: Target):

        if target.is_vehicle():
            return float(1)/6
        return float(1)/2


class SplinterRifle(SplinterWeapon):
    def __init__(self):
        super().__init__('splinter rifle',
                         0,
                         [
                            Profile(min_range=0, max_range=12, strength=1, shots=2, ap=0, damage=1),
                            Profile(min_range=12, max_range=24, strength=1, shots=1, ap=0, damage=1)
                         ])


class BlastPistol(Weapon):
    def __init__(self):
        super().__init__('blast pistol',
                         10,
                         [Profile(min_range=0, max_range=6, strength=8, shots=1, ap=4, damage=2)])


class Blaster(Weapon):
    def __init__(self):
        super().__init__('blast pistol',
                         15,
                         [Profile(min_range=0, max_range=18, strength=8, shots=1, ap=4, damage=2)])

class DarkLance(Weapon):
    def __init__(self):
        super().__init__('dark lance',
                         20,
                         [Profile(min_range=0, max_range=36, strength=8, shots=1, ap=4, damage=3.5)])


class HeatLance(Weapon):
    def __init__(self):
        super().__init__('heat lance',
                         25,
                         [Profile(min_range=9, max_range=18, strength=6, shots=1, ap=5, damage=3.5),
                          Profile(min_range=0, max_range=9, strength=6, shots=1, ap=5, damage=4.47)])


class MonoscytheMissile(Weapon):
    def __init__(self):
        super().__init__('monoscythe missile',
                         0,
                         [Profile(min_range=0, max_range=48, strength=6, shots=3.5, ap=0, damage=2)])

class NecrotoxinMissile(Weapon):

    def wound_probability(self, range_value: int, target: Target):

        if target.is_vehicle():
            return float(1)/6
        return float(5)/6

    def __init__(self):
        super().__init__('Necrotoxin missile',
                         0,
                         [Profile(min_range=0, max_range=48, strength=1, shots=6, ap=0, damage=1)])

class ShatterfieldMissile(Weapon):

    def is_reroll_wound(self):
        return True

    def __init__(self):
        super().__init__('shatterfield missile',
                         0,
                         [Profile(min_range=0, max_range=48, strength=7, shots=3.5, ap=1, damage=1)])

class SplinterCannon(SplinterWeapon):
    def __init__(self):
        super().__init__('splinter cannon',
                         15,
                         [
                            Profile(min_range=0, max_range=18, strength=1, shots=6, ap=0, damage=1),
                            Profile(min_range=18, max_range=36, strength=1, shots=3, ap=0, damage=1)
                         ])

class SplinterPistol(SplinterWeapon):
    def __init__(self):
        super().__init__('splinter pistol',
                         0,
                         [Profile(min_range=0, max_range=12, strength=1, shots=1, ap=0, damage=1)])


class Shardcarbine(SplinterWeapon):
    def __init__(self):
        super().__init__('shardcarbine',
                         0,
                         [Profile(min_range=0, max_range=18, strength=1, shots=3, ap=0, damage=1)])


class HeavyWraithCannon(Weapon):
    def __init__(self):
        super().__init__('Heavy Wraithcannon',
                         50,
                         [Profile(min_range=0, max_range=36, strength=10, shots=2, ap=4, damage=3.5)])


class ScatterLaser(Weapon):
    def __init__(self):
        super().__init__('Scatter Laser',
                         15,
                         [Profile(min_range=0, max_range=36, strength=6, shots=4, ap=0, damage=1)])


class Suncannon(Weapon):
    def __init__(self):
        super().__init__('Suncannon',
                         138,
                         [Profile(min_range=0, max_range=48, strength=6, shots=7, ap=3, damage=2)])
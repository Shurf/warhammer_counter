from .weapon import *

class GravWeapon(Weapon):
    def damage(self, target:Target, range_value:int) -> float:
        profile = self.profile(range_value)
        if profile is None:
            return 0
        if target.save() <= 3:
            return 2
        return profile.damage


class GravGun(GravWeapon):
    def __init__(self):
        super().__init__('grav gun',
                     15,
                     [Profile(min_range=0, max_range=12, strength=5, shots=2, ap=3, damage=1),
                      Profile(min_range=12, max_range=24, strength=5, shots=1, ap=3, damage=1)])

class MeltaGun(Weapon):
    def __init__(self):
        super().__init__('meltagun',
                         17,
                         [Profile(min_range=6, max_range=12, strength=8, shots=1, ap=4, damage=3.5),
                          Profile(min_range=0, max_range=6, strength=8, shots=1, ap=4, damage=4.47)])


class MultiMelta(Weapon):
    def __init__(self):
        super().__init__('Multi-Melta',
                         27,
                         [Profile(min_range=12, max_range=24, strength=8, shots=1, ap=4, damage=3.5),
                          Profile(min_range=0, max_range=12, strength=8, shots=1, ap=4, damage=4.47)])


class PlasmaGun(Weapon):
    def __init__(self):
        super().__init__('plasma gun',
                         13,
                         [Profile(min_range=0, max_range=12, strength=7, shots=2, ap=3, damage=1),
                          Profile(min_range=12, max_range=24, strength=7, shots=1, ap=3, damage=1)])


class PlasmaPistolOC(Weapon):
    def __init__(self):
        super().__init__('plasma pistol (oc)',
                         7,
                         [Profile(min_range=0, max_range=12, strength=7, shots=1, ap=3, damage=2)])


class PlasmaGunOC(Weapon):
    def __init__(self):
        super().__init__('plasma gun oc',
                         13,
                         [Profile(min_range=0, max_range=12, strength=8, shots=2, ap=3, damage=2),
                          Profile(min_range=12, max_range=24, strength=8, shots=1, ap=3, damage=2)])


class PlasmaCannon(Weapon):
    def __init__(self):
        super().__init__('plasma cannon',
                         21,
                         [Profile(min_range=0, max_range=36, strength=7, shots=2, ap=3, damage=1)])


class PlasmaCannonOC(Weapon):
    def __init__(self):
        super().__init__('plasma cannon',
                         21,
                         [Profile(min_range=0, max_range=36, strength=8, shots=2, ap=3, damage=2)])


class BoltPistol(Weapon):
    def __init__(self):
        super().__init__('bolt pistol',
                         0,
                         [Profile(min_range=0, max_range=12, strength=4, shots=1, ap=0, damage=1)])

class TwinBoltgun(Weapon):
    def __init__(self):
        super().__init__('twin boltgun',
                         2,
                         [Profile(min_range=0, max_range=12, strength=4, shots=4, ap=0, damage=1),
                          Profile(min_range=12, max_range=24, strength=4, shots=2, ap=0, damage=1)])

class Boltgun(Weapon):
    def __init__(self):
        super().__init__('boltgun',
                         0,
                         [Profile(min_range=0, max_range=12, strength=4, shots=2, ap=0, damage=1),
                          Profile(min_range=12, max_range=24, strength=4, shots=1, ap=0, damage=1)])


class BoltRifle(Weapon):
    def __init__(self):
        super().__init__('bolt rifle',
                         0,
                         [Profile(min_range=0, max_range=15, strength=4, shots=2, ap=1, damage=1),
                          Profile(min_range=12, max_range=30, strength=4, shots=1, ap=1, damage=1)])


class PlasmaTalon(Weapon):
    def __init__(self):
        super().__init__('plasma talon',
                         0,
                         [Profile(min_range=0, max_range=18, strength=7, shots=2, ap=3, damage=1)])

class PlasmaTalonOC(Weapon):
    def __init__(self):
        super().__init__('plasma talon OC',
                         0,
                         [Profile(min_range=0, max_range=18, strength=8, shots=2, ap=3, damage=2)])


class CenturionMissileLauncher(Weapon):
    def __init__(self):
        super().__init__('centurion missile launcher',
                         25,
                         [Profile(min_range=0, max_range=36, strength=8, shots=2, ap=2, damage=2)])


class GravCannonAmp(GravWeapon):
    def __init__(self):
        super().__init__('grav cannon (amp)',
                     28,
                     [Profile(min_range=0, max_range=24, strength=5, shots=4, ap=3, damage=1)])


class HurricaneBolter(Weapon):
    def __init__(self):
        super().__init__('hurricane bolter',
                         4,
                         [Profile(min_range=0, max_range=12, strength=4, shots=12, ap=0, damage=1),
                          Profile(min_range=12, max_range=24, strength=4, shots=6, ap=0, damage=1)])


class Lascannon(Weapon):
    def __init__(self):
        super().__init__('lascannon',
                         25,
                         [Profile(min_range=0, max_range=48, strength=9, shots=1, ap=3, damage=3.5)])


class HeavyBolter(Weapon):
    def __init__(self):
        super().__init__('heavy bolter',
                         10,
                         [Profile(min_range=0, max_range=36, strength=5, shots=3, ap=1, damage=1)])


class MissileLauncherKrak(Weapon):
    def __init__(self):
        super().__init__('missile launcher (krak)',
                         25,
                         [Profile(min_range=0, max_range=48, strength=8, shots=1, ap=2, damage=3.5)])

class MissileLauncherFrag(Weapon):
    def __init__(self):
        super().__init__('missile launcher (frag)',
                         25,
                         [Profile(min_range=0, max_range=48, strength=4, shots=3.5, ap=0, damage=1)])


class TwinAssaultCannon(Weapon):
    def __init__(self):
        super().__init__('twin assault cannon',
                         35,
                         [Profile(min_range=0, max_range=24, strength=6, shots=12, ap=1, damage=1)])


class TwinAcceleratorAutocannon(Weapon):
    def ap(self, range_value:int):
        return float(5)/6 + float(1)*3/6

    def __init__(self):
        super().__init__('twin accelerator autocannon',
                         75,
                         [Profile(min_range=0, max_range=48, strength=7, shots=8, ap=1, damage=2)])

class TwinAutocannon(Weapon):
    def __init__(self):
        super().__init__('Twin Autocannon',
                         33,
                         [Profile(min_range=0, max_range=48, strength=7, shots=4, ap=1, damage=2)])
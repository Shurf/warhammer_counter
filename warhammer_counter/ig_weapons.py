from .weapon import *

class Autocannon(Weapon):
    def __init__(self):
        super().__init__('Autocannon',
                         15,
                         [Profile(min_range=0, max_range=48, strength=7, shots=2, ap=1, damage=2)])


class BanebladeCannon(Weapon):
    def __init__(self):
        super().__init__('Baneblade Cannon',
                         0,
                         [Profile(min_range=0, max_range=72, strength=9, shots=7, ap=3, damage=3)])


class BattleCannon(Weapon):
    def __init__(self):
        super().__init__('Battle Cannon',
                         22,
                         [Profile(min_range=0, max_range=72, strength=8, shots=3.5, ap=2, damage=2)])


class DemolisherCannon(Weapon):
    def __init__(self):
        super().__init__('Demolisher Cannon',
                         40,
                         [Profile(min_range=0, max_range=24, strength=10, shots=2, ap=3, damage=3.5)])


class EarthshakerCannon(Weapon):
    def __init__(self):
        super().__init__('Earthshaker Cannon',
                         0,
                         [Profile(min_range=0, max_range=240, strength=9, shots=3.5, ap=2, damage=2)])


class ExecutionerPlasma(Weapon):
    def __init__(self):
        super().__init__('Executioner plasma',
                         20,
                         [Profile(min_range=0, max_range=36, strength=7, shots=3.5, ap=3, damage=1)])


class ExecutionerPlasmaOC(Weapon):
    def __init__(self):
        super().__init__('Executioner plasma OC',
                         20,
                         [Profile(min_range=0, max_range=36, strength=8, shots=3.5, ap=3, damage=2)])


class ExterminatorAutocannon(Weapon):
    def __init__(self):
        super().__init__('Autocannon',
                         25,
                         [Profile(min_range=0, max_range=48, strength=7, shots=4, ap=1, damage=2)])


class Flamer(Weapon):
    def is_autohit(self):
        return True
    def __init__(self):
        super().__init__('flamer',
                         7,
                         [Profile(min_range=0, max_range=8, strength=4, shots=3.5, ap=0, damage=1)])


class HeavyFlamer(Weapon):
    def is_autohit(self):
        return True
    def __init__(self):
        super().__init__('heavy flamer',
                         17,
                         [Profile(min_range=0, max_range=8, strength=5, shots=3.5, ap=1, damage=1)])


class HeavyBolter(Weapon):
    def __init__(self):
        super().__init__('heavy bolter',
                         8,
                         [Profile(min_range=0, max_range=36, strength=5, shots=3, ap=1, damage=1)])


class HellhammerCannon(Weapon):
    def __init__(self):
        super().__init__('hellhammer cannon',
                         0,
                         [Profile(min_range=0, max_range=36, strength=10, shots=7, ap=4, damage=3)])


class HotshotLasgun(Weapon):
    def __init__(self):
        super().__init__('hot-shot lasgun',
                         1,
                         [Profile(min_range=0, max_range=9, strength=3, shots=2, ap=2, damage=1),
                          Profile(min_range=9, max_range=18, strength=3, shots=1, ap=2, damage=1)])


class Lasgun(Weapon):
    def __init__(self):
        super().__init__('lasgun',
                         0,
                         [Profile(min_range=0, max_range=12, strength=3, shots=2, ap=0, damage=1),
                          Profile(min_range=12, max_range=24, strength=3, shots=1, ap=0, damage=1)])


class Lascannon(Weapon):
    def __init__(self):
        super().__init__('lascannon',
                         20,
                         [Profile(min_range=0, max_range=48, strength=9, shots=1, ap=3, damage=3.5)])


class MagmaCannon(Weapon):
    def __init__(self):
        super().__init__('magma cannon',
                         0,
                         [Profile(min_range=30, max_range=60, strength=10, shots=3.5, ap=5, damage=3.5),
                          Profile(min_range=0, max_range=30, strength=10, shots=4.47, ap=5, damage=4.47)])


class MeltaGun(Weapon):
    def __init__(self):
        super().__init__('meltagun',
                         12,
                         [Profile(min_range=6, max_range=12, strength=8, shots=1, ap=4, damage=3.5),
                          Profile(min_range=0, max_range=6, strength=8, shots=1, ap=4, damage=4.47)])


class MultiMelta(Weapon):
    def __init__(self):
        super().__init__('Multi-Melta',
                         20,
                         [Profile(min_range=12, max_range=24, strength=8, shots=1, ap=4, damage=3.5),
                          Profile(min_range=0, max_range=12, strength=8, shots=1, ap=4, damage=4.47)])


class MultiLaser(Weapon):
    def __init__(self):
        super().__init__('multi-laser',
                         9,
                         [Profile(min_range=0, max_range=36, strength=6, shots=3, ap=0, damage=1)])


class PlasmaGun(Weapon):
    def __init__(self):
        super().__init__('plasma gun',
                         7,
                         [Profile(min_range=0, max_range=12, strength=7, shots=2, ap=3, damage=1),
                          Profile(min_range=12, max_range=24, strength=7, shots=1, ap=3, damage=1)])


class PlasmaPistolOC(Weapon):
    def __init__(self):
        super().__init__('plasma pistol (oc)',
                         5,
                         [Profile(min_range=0, max_range=12, strength=7, shots=1, ap=3, damage=2)])


class PlasmaGunOC(Weapon):
    def __init__(self):
        super().__init__('plasma gun oc',
                         7,
                         [Profile(min_range=0, max_range=12, strength=8, shots=2, ap=3, damage=2),
                          Profile(min_range=12, max_range=24, strength=8, shots=1, ap=3, damage=2)])


class PlasmaCannon(Weapon):
    def __init__(self):
        super().__init__('plasma cannon',
                         15,
                         [Profile(min_range=0, max_range=36, strength=7, shots=2, ap=3, damage=1)])


class PlasmaCannonOC(Weapon):
    def __init__(self):
        super().__init__('plasma cannon',
                         15,
                         [Profile(min_range=0, max_range=36, strength=8, shots=2, ap=3, damage=2)])


class PunisherGatling(Weapon):
    def __init__(self):
        super().__init__('punisher gatling',
                         20,
                         [Profile(min_range=0, max_range=24, strength=5, shots=20, ap=0, damage=1)])


class QuakeCannon(Weapon):
    def __init__(self):
        super().__init__('quake cannon',
                         0,
                         [Profile(min_range=0, max_range=140, strength=14, shots=3.5, ap=4, damage=4)])


class StormEagleRocket(Weapon):
    def __init__(self):
        super().__init__('storm eagle rocket',
                         0,
                         [Profile(min_range=0, max_range=120, strength=10, shots=7, ap=2, damage=2)])


class StormswordSiegeCannon(Weapon):
    def __init__(self):
        super().__init__('stormsword siege cannon',
                         0,
                         [Profile(min_range=0, max_range=36, strength=10, shots=3.5, ap=4, damage=3.5)])


class TauroxBattleCannon(Weapon):
    def __init__(self):
        super().__init__('taurox battle cannon',
                         28,
                         [Profile(min_range=0, max_range=48, strength=7, shots=3.5, ap=1, damage=2)])


class TauroxGatlingCannon(Weapon):
    def __init__(self):
        super().__init__('taurox gatling cannon',
                         18,
                         [Profile(min_range=0, max_range=24, strength=4, shots=20, ap=0, damage=1)])


class TremorCannon(Weapon):
    def __init__(self):
        super().__init__('taurox gatling cannon',
                         0,
                         [Profile(min_range=0, max_range=60, strength=8, shots=7, ap=2, damage=3)])


class TwinHeavyFlamer(Weapon):
    def is_autohit(self):
        return True
    def __init__(self):
        super().__init__('twin heavy flamer',
                         30,
                         [Profile(min_range=0, max_range=8, strength=5, shots=7, ap=1, damage=1)])


class TwinHeavyBolter(Weapon):
    def __init__(self):
        super().__init__('twin heavy bolter',
                         14,
                         [Profile(min_range=0, max_range=36, strength=5, shots=6, ap=1, damage=1)])


class VanquisherBattleCannon(Weapon):
    def __init__(self):
        super().__init__('vanquisher battle cannon',
                         25,
                         [Profile(min_range=0, max_range=72, strength=8, shots=1, ap=3, damage=3.5)])


class VolcanoCannon(Weapon):
    def __init__(self):
        super().__init__('volcano cannon',
                         0,
                         [Profile(min_range=0, max_range=120, strength=16, shots=3.5, ap=5, damage=7)])


class VulcanMegaBolter(Weapon):
    def __init__(self):
        super().__init__('vulcan mega bolter',
                         0,
                         [Profile(min_range=0, max_range=60, strength=6, shots=20, ap=2, damage=2)])


class WyvernStormshardMortar(Weapon):
    def is_reroll_wound(self):
        return True

    def __init__(self):
        super().__init__('wyvern stormshard mortar',
                         0,
                         [Profile(min_range=0, max_range=48, strength=4, shots=14, ap=0, damage=1)])

class HeavyStubber(Weapon):
    def __init__(self):
        super().__init__('heavy stubber',
                         4,
                         [Profile(min_range=0, max_range=36, strength=4, shots=3, ap=0, damage=1)])


from .weapon import *

class TeslaWeapon(Weapon):
    def hit_probability(self, ballistic_skill, overwatch:bool):
        if self.is_autohit():
            return 1.0
        if overwatch:
            return float(1)/6
        return float(dice_side_count + 1 - ballistic_skill - 1)/dice_side_count + float(1)*3/dice_side_count


class TeslaCannon(TeslaWeapon):

    def __init__(self):
        super().__init__('Tesla cannon',
                         13,
                         [Profile(min_range=0, max_range=24, strength=6, shots=3, ap=0, damage=1)])


class TeslaCarbine(TeslaWeapon):

    def __init__(self):
        super().__init__('Tesla carbine',
                         9,
                         [Profile(min_range=0, max_range=24, strength=5, shots=2, ap=0, damage=1)])


class TeslaDestructor(TeslaWeapon):

    def __init__(self):
        super().__init__('Tesla destructor',
                         0,
                         [Profile(min_range=0, max_range=24, strength=7, shots=4, ap=0, damage=1)])


class TeslaSphere(TeslaWeapon):

    def __init__(self):
        super().__init__('Tesla sphere',
                         0,
                         [Profile(min_range=0, max_range=24, strength=7, shots=5, ap=0, damage=1)])


class GaussBlaster(Weapon):

    def __init__(self):
        super().__init__('gauss blaster',
                         9,
                         [Profile(min_range=0, max_range=12, strength=5, shots=2, ap=2, damage=1),
                          Profile(min_range=12, max_range=24, strength=5, shots=1, ap=2, damage=1)])


class GaussCannon(Weapon):

    def __init__(self):
        super().__init__('gauss cannon',
                         20,
                         [Profile(min_range=0, max_range=24, strength=5, shots=2, ap=3, damage=2)])


class HeavyGaussCannon(Weapon):

    def __init__(self):
        super().__init__('heavy gauss cannon',
                         32,
                         [Profile(min_range=0, max_range=36, strength=9, shots=1, ap=4, damage=3.5)])

class TwinHeavyGaussCannon(Weapon):

    def __init__(self):
        super().__init__('twin heavy gauss cannon',
                         64,
                         [Profile(min_range=0, max_range=36, strength=9, shots=2, ap=4, damage=3.5)])


class ParticleShredder(Weapon):

    def __init__(self):
        super().__init__('particle shredder',
                         41,
                         [Profile(min_range=0, max_range=24, strength=7, shots=6, ap=1, damage=2)])


class GaussFluxArc(Weapon):

    def __init__(self):
        super().__init__('gauss flux arc',
                         0,
                         [Profile(min_range=0, max_range=24, strength=5, shots=3, ap=2, damage=1)])


class GaussFlayer(Weapon):

    def __init__(self):
        super().__init__('gauss flayer',
                         0,
                         [Profile(min_range=0, max_range=12, strength=4, shots=2, ap=1, damage=1),
                          Profile(min_range=12, max_range=24, strength=4, shots=1, ap=1, damage=1)])


class DeathRay(Weapon):

    def __init__(self):
        super().__init__('death ray',
                         0,
                         [Profile(min_range=0, max_range=24, strength=10, shots=2, ap=4, damage=3.5)])


class ParticleBeamer(Weapon):

    def __init__(self):
        super().__init__('particle beamer',
                         10,
                         [Profile(min_range=0, max_range=24, strength=6, shots=3, ap=0, damage=1)])
__author__ = 'schrecknetuser'


class Target:
    def __init__(self, name: str, toughness: int, save: int, wounds: int, invulnerable: int):
        self.invulnerable_value = invulnerable
        self.name = name
        self.toughness_value = toughness
        self.save_value = save
        self.wounds_value = wounds

    def is_vehicle(self):
        return False

    def invulnerable(self):
        return self.invulnerable_value

    def toughness(self):
        return self.toughness_value

    def save(self):
        return self.save_value

    def wounds(self):
        return self.wounds_value


class Guardsman(Target):
    def __init__(self):
        super().__init__(name='guardsman', toughness=3, save=5, wounds=1, invulnerable=0)


class Ork(Target):
    def __init__(self):
        super().__init__(name='ork', toughness=4, save=6, wounds=1, invulnerable=0)


class Marine(Target):
    def __init__(self):
        super().__init__(name='marine', toughness=4, save=3, wounds=1, invulnerable=0)


class Terminator(Target):
    def __init__(self):
        super().__init__(name='terminator', toughness=4, save=2, wounds=2, invulnerable=5)


class Bike(Target):
    def __init__(self):
        super().__init__(name='bike', toughness=5, save=3, wounds=2, invulnerable=0)


class Piranha(Target):
    def is_vehicle(self):
        return True

    def __init__(self):
        super().__init__(name='piranha', toughness=5, save=4, wounds=6, invulnerable=0)


class Harpy(Target):
    def __init__(self):
        super().__init__(name='harpy', toughness=6, save=4, wounds=12, invulnerable=0)


class Manticore(Target):

    def is_vehicle(self):
        return True

    def __init__(self):
        super().__init__(name='manticore', toughness=7, save=3, wounds=11, invulnerable=0)

class Riptide(Target):

    def __init__(self):
        super().__init__(name='riptide', toughness=7, save=2, wounds=14, invulnerable=5)


class Rhino(Target):

    def is_vehicle(self):
        return True

    def __init__(self):
        super().__init__(name='rhino', toughness=7, save=3, wounds=12, invulnerable=0)


class LandRaider(Target):

    def is_vehicle(self):
        return True

    def __init__(self):
        super().__init__(name='land raider', toughness=8, save=2, wounds=16, invulnerable=0)

class ImperialKnight(Target):

    def is_vehicle(self):
        return True

    def __init__(self):
        super().__init__(name='IKnight', toughness=8, save=3, wounds=24, invulnerable=5)

default_targets = [
        Guardsman(),
        Ork(),
        Marine(),
        Terminator(),
        Bike(),
        Piranha(),
        Harpy(),
        Manticore(),
        Riptide(),
        Rhino(),
        LandRaider(),
        ImperialKnight()
    ]
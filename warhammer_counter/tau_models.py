__author__ = 'schrecknetuser'

from model import *
from tau_weapons import *

class Broadside(Model):
    def __init__(self):
        super().__init__('Broadside', 4, [Sms(), Sms(), Hymp(), Hymp()], 80)


class Riptide(Model):
    def __init__(self, name_addon:str, weapons):
        super().__init__('Riptide ' + name_addon, 4, weapons, 209)


class RiptideIaNovaPlasma(Riptide):
    def __init__(self):
        super().__init__('ia nova plasma', [IANova(), Plasma(), Plasma()])


class RiptideIaNovaSms(Riptide):
    def __init__(self):
        super().__init__('ia nova sms', [IANova(), Sms(), Sms()])


class RiptideBurstNovaPlasma(Riptide):
    def __init__(self):
        super().__init__('burst nova plasma', [HvyBurstCannon(), Plasma(), Plasma()])


class RiptideBurstNovaSms(Riptide):
    def __init__(self):
        super().__init__('burst nova sms', [HvyBurstCannon(), Sms(), Sms()])


class Stormsurge(Model):

    def bs(self):
        return 4

    def preset_weapons(self):
        return [ClusterRocketSystem(), Sms(), Sms()]

    def name(self):
        return 'Stormsurge '

    def __init__(self, name_addon:str, weapons_addon):
        super().__init__(self.name() + name_addon, self.bs(), self.preset_weapons() + weapons_addon, 180 + 40)


class StormsurgeAnchored(Stormsurge):

    def bs(self):
        return 3

    def name(self):
        return 'Stormsurge (anchored) '


class StormsurgeBlastCannonShort(Stormsurge):
    def __init__(self):
        super().__init__('blastcannon short', [PulseBlastcannonShort(), Flamer(), Flamer()])


class StormsurgeBlastCannonMedium(Stormsurge):
    def __init__(self):
        super().__init__('blastcannon medium', [PulseBlastcannonMedium(), Flamer(), Flamer()])


class StormsurgeBlastCannonLong(Stormsurge):
    def __init__(self):
        super().__init__('blastcannon long', [PulseBlastcannonLong(), Flamer(), Flamer()])


class StormsurgePulseDriver(Stormsurge):
    def __init__(self):
        super().__init__('pulse driver', [PulseDriverCannon(), Flamer(), Flamer()])

class StormsurgePulseDriverAnchored(StormsurgeAnchored):
    def __init__(self):
        super().__init__('pulse driver', [PulseDriverCannon(), Flamer(), Flamer()])

class FireWarrior(Model):
    def __init__(self):
        super().__init__('Fire Warrior (rifle)', 4, [PulseRifle()], 8)

class CommanderFlamerTwoFusion(Model):
    def __init__(self):
        super().__init__('Commander (flamer, 2xfusion)', 2, [FusionBlaster(), FusionBlaster(), Flamer()], 76)

class CrisisSuit(Model):

    def cost(self):
        return 42

    def name(self):
        return 'Crisis suit '

    def __init__(self, name_addon:str, weapons):
        super().__init__(self.name() + name_addon, 4, weapons, self.cost())


class CrisisSuitThreeMissilePods(CrisisSuit):
    def __init__(self):
        super().__init__("3 mp", [MissilePod(), MissilePod(), MissilePod()])

class CrisisSuitTwoMissilePodsATS(CrisisSuit):

    def ap_modifier(self):
        return 1

    def cost(self):
        return super().cost() + 8

    def __init__(self):
        super().__init__("2 mp ATS", [MissilePod(), MissilePod()])

tau_models_list = [
    FireWarrior(),
    CommanderFlamerTwoFusion(),
    CrisisSuitThreeMissilePods(),
    CrisisSuitTwoMissilePodsATS(),
    Broadside(),
    RiptideIaNovaPlasma(),
    RiptideBurstNovaPlasma(),
    RiptideIaNovaSms(),
    RiptideBurstNovaSms(),
    StormsurgeBlastCannonShort(),
    StormsurgeBlastCannonMedium(),
    StormsurgeBlastCannonLong(),
    StormsurgePulseDriver(),
    StormsurgePulseDriverAnchored()
]
from model import *
from ik_weapons import *

errant = Model(name='Errant', ballistic=3, weapons=[ThermalCannon(), HeavyStubber()], base_cost=320)
errant_ironstorm = Model(name='Errant ironstorm', ballistic=3, weapons=[ThermalCannon(), HeavyStubber(), IronstormMissilePod()], base_cost=320)
errant_stormspear = Model(name='Errant stormspear', ballistic=3, weapons=[ThermalCannon(), HeavyStubber(), StormspearRocketPod()], base_cost=320)

paladin = Model(name='Paladin', ballistic=3, weapons=[RapidFireBattleCannon(), HeavyStubber(), HeavyStubber()], base_cost=320)
paladin_ironstorm = Model(name='Paladin ironstorm', ballistic=3, weapons=[RapidFireBattleCannon(), HeavyStubber(), HeavyStubber(), IronstormMissilePod()], base_cost=320)
paladin_stormspear = Model(name='Paladin stormspear', ballistic=3, weapons=[RapidFireBattleCannon(), HeavyStubber(), HeavyStubber(), StormspearRocketPod()], base_cost=320)

warden = Model(name='Warden', ballistic=3, weapons=[AvengerGatlingCannon(), HeavyStubber(), HeavyFlamer()], base_cost=320)
warden_ironstorm = Model(name='Warden ironstorm', ballistic=3, weapons=[AvengerGatlingCannon(), HeavyStubber(), HeavyFlamer(), IronstormMissilePod()], base_cost=320)
warden_stormspear = Model(name='Warden stormspear', ballistic=3, weapons=[AvengerGatlingCannon(), HeavyStubber(), HeavyFlamer(), StormspearRocketPod()], base_cost=320)

crusader_tc = Model(name='Crusader TC', ballistic=3, weapons=[AvengerGatlingCannon(), HeavyFlamer(), ThermalCannon(), HeavyStubber()], base_cost=320)
crusader_tc_ironstorm = Model(name='Crusader TC ironstorm', ballistic=3, weapons=[AvengerGatlingCannon(), HeavyFlamer(), ThermalCannon(), HeavyStubber(), IronstormMissilePod()], base_cost=320)
crusader_tc_stormspear = Model(name='Crusader TC stormspear', ballistic=3, weapons=[AvengerGatlingCannon(), HeavyFlamer(), ThermalCannon(), HeavyStubber(), StormspearRocketPod()], base_cost=320)

crusader_bc = Model(name='Crusader BC', ballistic=3, weapons=[AvengerGatlingCannon(), HeavyFlamer(), RapidFireBattleCannon(), HeavyStubber()], base_cost=320)
crusader_bc_ironstorm = Model(name='Crusader BC ironstorm', ballistic=3, weapons=[AvengerGatlingCannon(), HeavyFlamer(), RapidFireBattleCannon(), HeavyStubber(), HeavyStubber(), IronstormMissilePod()], base_cost=320)
crusader_bc_stormspear = Model(name='Crusader BC stormspear', ballistic=3, weapons=[AvengerGatlingCannon(), HeavyFlamer(), RapidFireBattleCannon(), HeavyStubber(), HeavyStubber(), StormspearRocketPod()], base_cost=320)

ik_models_list = [
    errant,
    errant_ironstorm,
    errant_stormspear,
    paladin,
    paladin_ironstorm,
    paladin_stormspear,
    warden,
    warden_ironstorm,
    warden_stormspear,
    crusader_tc,
    crusader_tc_ironstorm,
    crusader_tc_stormspear,
    crusader_bc,
    crusader_bc_ironstorm,
    crusader_bc_stormspear,
]

ik_filtered_models_list = [
    warden_stormspear,
    crusader_tc_stormspear,
    crusader_bc_stormspear,
]
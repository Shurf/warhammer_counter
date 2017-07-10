from model import *
from ig_weapons import *

guardsman = Model(name='guardsman', ballistic=4, weapons=[Lasgun()], base_cost=4)
las_plas_inf_squad_oc = Model(name='las plas inf squad (oc)', ballistic=4, weapons=[Lasgun(), Lasgun(), Lasgun(), Lasgun(), Lasgun(), Lasgun(), PlasmaGunOC(), PlasmaPistolOC(), Lascannon()], base_cost=40)
scion = Model(name='scion (hs lasgun)', ballistic=3, weapons=[HotshotLasgun()], base_cost=10)
scion_melta = Model(name='scion (melta)', ballistic=3, weapons=[MeltaGun()], base_cost=10)
scion_melta_inc_tempestor = Model(name='scion (melta) w/tempestor', ballistic=3, weapons=[MeltaGun()], base_cost=20)
scion_plasma = Model(name='scion (plasma)', ballistic=3, weapons=[PlasmaGun()], base_cost=10)
scion_plasma_oc = Model(name='scion (plasma (oc))', ballistic=3, weapons=[PlasmaGunOC()], base_cost=10)
scion_plasma_oc_inc_tempestor = Model(name='scion (plasma (oc)) w/tempestor', ballistic=3, weapons=[PlasmaGunOC()], base_cost=20)
scion_troop_plasma = Model(name='scion troop (plasma (oc))', ballistic=3, weapons=[PlasmaGunOC(), PlasmaGunOC(), PlasmaPistolOC(), HotshotLasgun(), HotshotLasgun()], base_cost=50)
scion_troop_plasma_no_pistol = Model(name='scion troop (plasma (oc) no pistol)', ballistic=3, weapons=[PlasmaGunOC(), PlasmaGunOC(), HotshotLasgun(), HotshotLasgun(), HotshotLasgun()], base_cost=50)
scion_troop_melta = Model(name='scion troop (melta)', ballistic=3, weapons=[MeltaGun(), MeltaGun(), HotshotLasgun(), HotshotLasgun(), HotshotLasgun()], base_cost=50)
hvy_wpn_team_lascannon = Model(name='HWT (lascannon)', ballistic=4, weapons=[Lascannon()], base_cost=4)
hvy_wpn_team_autocannon = Model(name='HWT (autocannon)', ballistic=4, weapons=[Autocannon()], base_cost=4)
armoured_sentinel_autocannon = Model(name='Arm. Sentinel (AC)', ballistic=4, weapons=[Autocannon()], base_cost=40)
taurox_autocannon = Model(name='Taurox', ballistic=4, weapons=[Autocannon(), Autocannon()], base_cost=55)
basilisk = Model(name='Basilisk', ballistic=4, weapons=[EarthshakerCannon(), HeavyBolter()], base_cost=100)
wyvern = Model(name='Wyvern', ballistic=4, weapons=[WyvernStormshardMortar(), HeavyBolter()], base_cost=85)
manticore = Model(name='manticore', ballistic=4, weapons=[StormEagleRocket(), HeavyBolter()], base_cost=125)

leman_russ_bt = Model(name='LRBT', ballistic=4, weapons=[BattleCannon(), HeavyBolter()], base_cost=132)
leman_russ_bt_lc = Model(name='LRBT LC', ballistic=4, weapons=[BattleCannon(), Lascannon()], base_cost=132)
leman_russ_bt_lc_mm = Model(name='LRBT LC MM', ballistic=4, weapons=[BattleCannon(), Lascannon(), MultiMelta(), MultiMelta()], base_cost=132)

leman_russ_dem = Model(name='LRD', ballistic=4, weapons=[DemolisherCannon(), HeavyBolter()], base_cost=132)
leman_russ_dem_lc = Model(name='LRD LC', ballistic=4, weapons=[DemolisherCannon(), Lascannon()], base_cost=132)
leman_russ_dem_lc_mm = Model(name='LRD LC MM', ballistic=4, weapons=[DemolisherCannon(), Lascannon(), MultiMelta(), MultiMelta()], base_cost=132)

leman_russ_punisher = Model(name='LRP', ballistic=4, weapons=[PunisherGatling(), HeavyBolter()], base_cost=132)
leman_russ_punisher_hb = Model(name='LRP HB', ballistic=4, weapons=[PunisherGatling(), HeavyBolter(), HeavyBolter(), HeavyBolter()], base_cost=132)

leman_russ_exterminator = Model(name='LRE', ballistic=4, weapons=[ExterminatorAutocannon(), HeavyBolter()], base_cost=132)
leman_russ_exterminator_hb = Model(name='LRE HB', ballistic=4, weapons=[ExterminatorAutocannon(), HeavyBolter(), HeavyBolter(), HeavyBolter()], base_cost=132)

baneblade = Model(name='baneblade', ballistic=4, weapons=[Autocannon(), DemolisherCannon(), BanebladeCannon(), TwinHeavyBolter()], base_cost=430)
baneblade_sponsons = Model(name='baneblade sponsons', ballistic=4,
                  weapons=[Autocannon(), DemolisherCannon(), BanebladeCannon(), TwinHeavyBolter(),
                           Lascannon(), Lascannon(), Lascannon(), Lascannon(), TwinHeavyBolter(), TwinHeavyBolter(), TwinHeavyBolter(), TwinHeavyBolter()], base_cost=430)

banehammer = Model(name='banehammer', ballistic=4, weapons=[TremorCannon(), TwinHeavyBolter()], base_cost=410)
banehammer_sponsons = Model(name='banehammer sponsons', ballistic=4,
                  weapons=[TremorCannon(), TwinHeavyBolter(),
                           Lascannon(), Lascannon(), Lascannon(), Lascannon(), TwinHeavyBolter(), TwinHeavyBolter(), TwinHeavyBolter(), TwinHeavyBolter()], base_cost=410)

banesword = Model(name='banesword', ballistic=4, weapons=[QuakeCannon(), TwinHeavyBolter()], base_cost=390)
banesword_sponsons = Model(name='banesword sponsons', ballistic=4,
                  weapons=[QuakeCannon(), TwinHeavyBolter(),
                           Lascannon(), Lascannon(), Lascannon(), Lascannon(), TwinHeavyBolter(), TwinHeavyBolter(), TwinHeavyBolter(), TwinHeavyBolter()], base_cost=390)


doomhammer = Model(name='doomhammer', ballistic=4, weapons=[MagmaCannon(), TwinHeavyBolter()], base_cost=420)
doomhammer_sponsons = Model(name='doomhammer sponsons', ballistic=4,
                  weapons=[MagmaCannon(), TwinHeavyBolter(),
                           Lascannon(), Lascannon(), Lascannon(), Lascannon(), TwinHeavyBolter(), TwinHeavyBolter(), TwinHeavyBolter(), TwinHeavyBolter()], base_cost=420)

hellhammer = Model(name='hellhammer', ballistic=4, weapons=[Autocannon(), DemolisherCannon(), HellhammerCannon(), TwinHeavyBolter(), Lasgun()], base_cost=450)
hellhammer_sponsons = Model(name='hellhammer sponsons', ballistic=4,
                  weapons=[Autocannon(), DemolisherCannon(), HellhammerCannon(), TwinHeavyBolter(), Lasgun(),
                           Lascannon(), Lascannon(), Lascannon(), Lascannon(), TwinHeavyBolter(), TwinHeavyBolter(), TwinHeavyBolter(), TwinHeavyBolter()], base_cost=450)


shadowsword = Model(name='shadowsword', ballistic=4, weapons=[VolcanoCannon(), TwinHeavyBolter()], base_cost=430)
shadowsword_sponsons = Model(name='shadowsword sponsons', ballistic=4,
                  weapons=[VolcanoCannon(), TwinHeavyBolter(),
                           Lascannon(), Lascannon(), Lascannon(), Lascannon(), TwinHeavyBolter(), TwinHeavyBolter(), TwinHeavyBolter(), TwinHeavyBolter()], base_cost=430)


stormsword = Model(name='stormsword', ballistic=4, weapons=[StormswordSiegeCannon(), TwinHeavyBolter()], base_cost=390)
stormsword_sponsons = Model(name='stormsword sponsons', ballistic=4,
                  weapons=[StormswordSiegeCannon(), TwinHeavyBolter(),
                           Lascannon(), Lascannon(), Lascannon(), Lascannon(), TwinHeavyBolter(), TwinHeavyBolter(), TwinHeavyBolter(), TwinHeavyBolter()], base_cost=390)

stormlord = Model(name='stormlord', ballistic=4, weapons=[VulcanMegaBolter(), TwinHeavyBolter(), HeavyStubber(), HeavyStubber()], base_cost=430)
stormlord_sponsons = Model(name='stormlord sponsons', ballistic=4,
                  weapons=[VulcanMegaBolter(), TwinHeavyBolter(), HeavyStubber(), HeavyStubber(),
                           Lascannon(), Lascannon(), Lascannon(), Lascannon(), TwinHeavyBolter(), TwinHeavyBolter(), TwinHeavyBolter(), TwinHeavyBolter()], base_cost=430)

ig_models_list = [
    guardsman,
    las_plas_inf_squad_oc,
    scion,
    scion_melta,
    scion_plasma,
    scion_plasma_oc,
    scion_plasma_oc_inc_tempestor,
    scion_troop_plasma,
    scion_troop_melta,
    scion_troop_plasma_no_pistol,
    hvy_wpn_team_lascannon,
    hvy_wpn_team_autocannon,
    armoured_sentinel_autocannon,
    taurox_autocannon,
    basilisk,
    wyvern,
    manticore,
    leman_russ_bt,
    leman_russ_bt_lc,
    leman_russ_bt_lc_mm,
    leman_russ_dem,
    leman_russ_dem_lc,
    leman_russ_dem_lc_mm,
    leman_russ_punisher,
    leman_russ_punisher_hb,
    leman_russ_exterminator,
    leman_russ_exterminator_hb,
    baneblade,
    baneblade_sponsons,
    banehammer,
    banehammer_sponsons,
    banesword,
    banesword_sponsons,
    doomhammer,
    doomhammer_sponsons,
    hellhammer,
    hellhammer_sponsons,
    shadowsword,
    shadowsword_sponsons,
    stormsword,
    stormsword_sponsons,
    stormlord,
    stormlord_sponsons
]


ig_leman_russ_list = [
    leman_russ_bt,
    leman_russ_bt_lc,
    leman_russ_bt_lc_mm,
    leman_russ_dem,
    leman_russ_dem_lc,
    leman_russ_dem_lc_mm,
    leman_russ_punisher,
    leman_russ_punisher_hb,
    leman_russ_exterminator,
    leman_russ_exterminator_hb
]

ig_baneblade_list = [
    baneblade,
    baneblade_sponsons,
    banehammer,
    banehammer_sponsons,
    banesword,
    banesword_sponsons,
    doomhammer,
    doomhammer_sponsons,
    hellhammer,
    hellhammer_sponsons,
    shadowsword,
    shadowsword_sponsons,
    stormsword,
    stormsword_sponsons,
    stormlord,
    stormlord_sponsons
]

ig_filtered_models_list = [
    #guardsman,
    las_plas_inf_squad_oc,
    scion_melta_inc_tempestor,
    #scion_plasma,
    #scion_plasma_oc,
    scion_plasma_oc_inc_tempestor,
    scion_troop_plasma,
    scion_troop_plasma_no_pistol,
    scion_troop_melta,
    hvy_wpn_team_lascannon,
    hvy_wpn_team_autocannon,
    wyvern,
    manticore,
    leman_russ_bt_lc_mm,
    leman_russ_dem_lc_mm,
    leman_russ_punisher_hb,
    baneblade_sponsons,
    hellhammer_sponsons,
    shadowsword_sponsons,
    stormlord_sponsons
]
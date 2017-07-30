from .model import *
from .de_weapons import *

kabalite = Model(name='kabalite', ballistic=3, weapons=[SplinterRifle()], base_cost=7)
kabalite_squad = Model(name='kabalite squad', ballistic=3, weapons=[SplinterRifle(), SplinterRifle(), SplinterRifle(), SplinterRifle(), Blaster()], base_cost=35)
kabalite_squad_pistol = Model(name='kabalite squad (bp)', ballistic=3, weapons=[SplinterRifle(), SplinterRifle(), SplinterRifle(), BlastPistol(), Blaster()], base_cost=35)

trueborn_squad = Model(name='trueborn squad (blaster)', ballistic=3, weapons=[SplinterRifle(), Blaster(), Blaster(), Blaster(), Blaster()], base_cost=55)
trueborn_squad_pistol = Model(name='trueborn squad (blaster+bp)', ballistic=3, weapons=[BlastPistol(), Blaster(), Blaster(), Blaster(), Blaster()], base_cost=55)
trueborn_squad_lances = Model(name='trueborn squad (lances)', ballistic=3, weapons=[SplinterRifle(), SplinterRifle(), SplinterRifle(), DarkLance(), DarkLance()], base_cost=55)

scatter_bike = Model(name='scatter bike', ballistic=3, weapons=[ScatterLaser()], base_cost=20)

raider = Model(name='raider', ballistic=3, weapons=[DarkLance()], base_cost=95)
venom_rifles = Model(name='venom (rifles)', ballistic=3, weapons=[SplinterCannon(), SplinterRifle(), SplinterRifle()], base_cost=65)
venom_cannon = Model(name='venom (cannon)', ballistic=3, weapons=[SplinterCannon(), SplinterCannon()], base_cost=65)

razorwing_monoscythe_rifles = Model(name='razorwing (rifles+monoscythe)', ballistic=3, weapons=[DarkLance(), DarkLance(), SplinterRifle(), SplinterRifle(), MonoscytheMissile()], base_cost=115)
razorwing_necrotoxin_rifles = Model(name='razorwing (rifles+necrotoxin)', ballistic=3, weapons=[DarkLance(), DarkLance(), SplinterRifle(), SplinterRifle(), NecrotoxinMissile()], base_cost=115)
razorwing_shatterfield_rifles = Model(name='razorwing (rifles+shatterfield)', ballistic=3, weapons=[DarkLance(), DarkLance(), SplinterRifle(), SplinterRifle(), ShatterfieldMissile()], base_cost=115)

razorwing_monoscythe_cannon = Model(name='razorwing (cannon+monoscythe)', ballistic=3, weapons=[DarkLance(), DarkLance(), SplinterCannon(), MonoscytheMissile()], base_cost=115)
razorwing_necrotoxin_cannon = Model(name='razorwing (cannon+necrotoxin)', ballistic=3, weapons=[DarkLance(), DarkLance(), SplinterCannon(), NecrotoxinMissile()], base_cost=115)
razorwing_shatterfield_cannon = Model(name='razorwing (cannon+shatterfield)', ballistic=3, weapons=[DarkLance(), DarkLance(), SplinterCannon(), ShatterfieldMissile()], base_cost=115)

scourges_squad_lances = Model(name='scourge squad (lances)', ballistic=3, weapons=[Shardcarbine(), DarkLance(), DarkLance(), DarkLance(), DarkLance()], base_cost=90)
scourges_squad_blasters = Model(name='scourge squad (blasters)', ballistic=3, weapons=[Shardcarbine(), Blaster(), Blaster(), Blaster(), Blaster()], base_cost=90)
scourges_squad_heat = Model(name='scourge squad (heat)', ballistic=3, weapons=[Shardcarbine(), HeatLance(), HeatLance(), HeatLance(), HeatLance()], base_cost=90)

ravager = Model(name='ravager', ballistic=3, weapons=[DarkLance(), DarkLance(), DarkLance()], base_cost=95)

wraithknight = Model(name='WK/w_cannon', ballistic=3, weapons=[HeavyWraithCannon(), HeavyWraithCannon(), ScatterLaser(), ScatterLaser()], base_cost=402)
wraithknight_suncannon = Model(name='WK/suncannon', ballistic=3, weapons=[Suncannon(), ScatterLaser(), ScatterLaser()], base_cost=402)

de_models_list = [
    kabalite,
    kabalite_squad,
    kabalite_squad_pistol,
    trueborn_squad,
    trueborn_squad_pistol,
    trueborn_squad_lances,
    raider,
    venom_rifles,
    venom_cannon,
    scatter_bike,
    razorwing_monoscythe_rifles,
    razorwing_necrotoxin_rifles,
    razorwing_shatterfield_rifles,
    razorwing_monoscythe_cannon,
    razorwing_necrotoxin_cannon,
    razorwing_shatterfield_cannon,
    scourges_squad_lances,
    scourges_squad_blasters,
    scourges_squad_heat,
    ravager,
    wraithknight,
    wraithknight_suncannon
]

razorwings = [
    razorwing_monoscythe_rifles,
    razorwing_necrotoxin_rifles,
    razorwing_shatterfield_rifles,
    razorwing_monoscythe_cannon,
    razorwing_necrotoxin_cannon,
    razorwing_shatterfield_cannon
]

de_filtered_models_list = [
    kabalite,
    kabalite_squad,
    kabalite_squad_pistol,
    trueborn_squad,
    trueborn_squad_pistol,
    trueborn_squad_lances,
    raider,
    venom_rifles,
    venom_cannon,
    razorwing_monoscythe_rifles,
    razorwing_necrotoxin_rifles,
    razorwing_shatterfield_rifles,
    razorwing_monoscythe_cannon,
    razorwing_necrotoxin_cannon,
    razorwing_shatterfield_cannon,
    scourges_squad_heat,
    ravager
]
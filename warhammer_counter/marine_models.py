from .model import *
from .marine_weapons import *

marine = Model(name='marine', ballistic=3, weapons=[Boltgun(), BoltPistol()], base_cost=13)
intercessor = Model(name='intercessor', ballistic=3, weapons=[BoltRifle(), BoltPistol()], base_cost=20)
bike_melta = Model(name='Bike(unit)/Melta', ballistic=3, weapons=[MeltaGun(), TwinBoltgun(), MeltaGun(), TwinBoltgun(), BoltPistol()], base_cost=31*3)
bike_plasma = Model(name='Bike(unit)/Plasma', ballistic=3, weapons=[PlasmaGun(), TwinBoltgun(), PlasmaGun(), TwinBoltgun(), BoltPistol()], base_cost=31*3)
bike_plasma_oc = Model(name='Bike(unit)/PlasmaOC', ballistic=3, weapons=[PlasmaGunOC(), TwinBoltgun(), PlasmaGunOC(), TwinBoltgun(), BoltPistol()], base_cost=31*3)
bike_grav = Model(name='Bike(unit)/Grav', ballistic=3, weapons=[GravGun(), TwinBoltgun(), GravGun(), TwinBoltgun(), BoltPistol()], base_cost=31*3)
black_knight = Model(name='Black Knight(unit)', ballistic=3, weapons=[PlasmaTalon(), BoltPistol(), PlasmaTalon(), BoltPistol(), PlasmaTalon(), BoltPistol()], base_cost=50*3)
black_knight_oc = Model(name='Black Knight(unit) OC', ballistic=3, weapons=[PlasmaTalonOC(), BoltPistol(), PlasmaTalonOC(), BoltPistol(), PlasmaTalonOC(), BoltPistol()], base_cost=50*3)

centurion_grav_bolters = Model(name='Centurion/grav+bolters', ballistic=3, weapons=[GravCannonAmp(), HurricaneBolter()], base_cost=65)
centurion_grav_missiles = Model(name='Centurion/grav+missiles', ballistic=3, weapons=[GravCannonAmp(), CenturionMissileLauncher()], base_cost=65)

centurion_lascannon_bolters = Model(name='Centurion/lascannon+bolters', ballistic=3, weapons=[Lascannon(), Lascannon(), HurricaneBolter()], base_cost=65)
centurion_lascannon_missiles = Model(name='Centurion/lascannon+missiles', ballistic=3, weapons=[Lascannon(), Lascannon(), CenturionMissileLauncher()], base_cost=65)

devastator_lascannon_squad = Model(name='Devastator/lascannon (unit)', ballistic=3, weapons=[Lascannon(), Lascannon(), Lascannon(), Lascannon(), Boltgun(),
                                                                                             BoltPistol(), BoltPistol(), BoltPistol(), BoltPistol(), BoltPistol()], base_cost=13*5)

devastator_missiles_krak_squad = Model(name='Devastator/krak missile (unit)', ballistic=3, weapons=[MissileLauncherKrak(), MissileLauncherKrak(), MissileLauncherKrak(), MissileLauncherKrak(), Boltgun(),
                                                                                             BoltPistol(), BoltPistol(), BoltPistol(), BoltPistol(), BoltPistol()], base_cost=13*5)
devastator_missiles_frag_squad = Model(name='Devastator/frag missile (unit)', ballistic=3, weapons=[MissileLauncherFrag(), MissileLauncherFrag(), MissileLauncherFrag(), MissileLauncherFrag(), Boltgun(),
                                                                                             BoltPistol(), BoltPistol(), BoltPistol(), BoltPistol(), BoltPistol()], base_cost=13*5)

sicaran_naked = Model(name='sicaran', ballistic=3, weapons=[TwinAcceleratorAutocannon(), HeavyBolter()], base_cost=155)
sicaran_bolters = Model(name='sicaran (bolters)', ballistic=3, weapons=[TwinAcceleratorAutocannon(), HeavyBolter(), HeavyBolter(), HeavyBolter()], base_cost=155)
sicaran_lascannons = Model(name='sicaran (bolters)', ballistic=3, weapons=[TwinAcceleratorAutocannon(), HeavyBolter(), Lascannon(), Lascannon()], base_cost=155)

razorback_assault = Model(name='Razorback/AC', ballistic=3, weapons=[TwinAssaultCannon()], base_cost=65)

dreadnought_auto = Model(name='Dreadnought/Autocannon', ballistic=3, weapons=[TwinAutocannon(), TwinAutocannon()], base_cost=70)

marine_models_list = [
    marine,
    intercessor,
    bike_melta,
    bike_plasma,
    bike_plasma_oc,
    bike_grav,
    black_knight,
    black_knight_oc,
    centurion_grav_bolters,
    centurion_grav_missiles,
    centurion_lascannon_bolters,
    centurion_lascannon_missiles,
    devastator_lascannon_squad,
    devastator_missiles_krak_squad,
    devastator_missiles_frag_squad,
    sicaran_naked,
    sicaran_bolters,
    sicaran_lascannons,
    razorback_assault,
    dreadnought_auto
]
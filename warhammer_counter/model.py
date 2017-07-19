__author__ = 'schrecknetuser'

import typing
from .weapon import *
from .targets import *

class Model:
    def __init__(self, name:str, ballistic:float, weapons:typing.List[Weapon], base_cost:int):
        self.ballistic_value = ballistic
        self.name = name
        self.weapons = weapons
        self.base_cost = base_cost

    def hundreds_of_points(self):
        total_cost = self.base_cost
        total_cost += sum([x.point_cost() for x in self.weapons])
        return float(total_cost)/100

    def ap_modifier(self):
        return 0

    def damage_probability(self, weapon: Weapon, range_value: int, target: Target) -> float:
        return weapon.wound_probability(range_value=range_value, target=target)

    def unsaved_wound_probability(self, ap: int, save:int, invulnerable:int) -> float:
        total_save = save + ap + self.ap_modifier()
        if invulnerable != 0 and invulnerable < total_save:
            total_save = invulnerable

        if total_save > dice_side_count:
            return 1.0
        return float(total_save - 1)/dice_side_count

    def hit_probability(self, weapon, overwatch:bool):
        return weapon.hit_probability(self.ballistic_value, overwatch)


    def divider(self):
        #return 1
        return self.hundreds_of_points()

    def wound_count(self, target: Target, range_value:int, overwatch:bool) -> float:

        result = 0.0
        for weapon in self.weapons:
            wound_probability = self.damage_probability(weapon, range_value, target)
            unsaved_probability = self.unsaved_wound_probability(weapon.ap(range_value), target.save(), target.invulnerable())
            expected_dmg = min(weapon.damage(target, range_value), target.wounds())
            hit_probability = self.hit_probability(weapon, overwatch)
            result += wound_probability*unsaved_probability*expected_dmg*weapon.shots(range_value)*hit_probability
        return result

    def divided_result(self, target: Target, range_value:int, overwatch:bool) -> float:
        float_result = self.wound_count(target, range_value, overwatch)/self.divider()
        return float(int(float_result*100))/100
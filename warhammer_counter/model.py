__author__ = 'schrecknetuser'

import typing
from weapon import *
from targets import *
dice_side_count = 6

class Model:
    def __init__(self, name:str, ballistic:int, weapons:typing.List[Weapon], base_cost:int):
        self.ballistic = ballistic
        self.name = name
        self.weapons = weapons
        self.base_cost = base_cost

    def hundreds_of_points(self):
        total_cost = self.base_cost
        total_cost += sum([x.point_cost() for x in self.weapons])
        return float(total_cost)/100

    def damage_probability(self, strength: int, toughness: int) -> float:
        if strength == 0:
            return 0
        if strength*2 <= toughness:
            return float(1)/6
        if strength < toughness:
            return float(2)/6
        if strength == toughness:
            return float(1)/2
        if strength >= toughness*2:
            return float(5)/6
        if strength > toughness:
            return float(2)/3

    def unsaved_wound_probability(self, ap: int, save:int, invulnerable:int) -> float:
        total_save = save + ap
        if invulnerable != 0 and invulnerable < total_save:
            total_save = invulnerable

        if total_save > dice_side_count:
            return 1.0
        return float(total_save - 1)/dice_side_count

    def hit_probability(self, weapon):
        if weapon.is_autohit():
            return 1.0
        return float(dice_side_count + 1 - self.ballistic)/dice_side_count

    def divider(self):
        #return 1
        return self.hundreds_of_points()

    def wound_count(self, target: Target, range_value:int) -> float:

        result = 0.0
        for weapon in self.weapons:
            wound_probability = self.damage_probability(weapon.strength(range_value), target.toughness())
            unsaved_probability = self.unsaved_wound_probability(weapon.ap(range_value), target.save(), target.invulnerable())
            expected_dmg = min(weapon.damage(range_value), target.wounds())
            hit_probability = self.hit_probability(weapon)
            result += wound_probability*unsaved_probability*expected_dmg*weapon.shots(range_value)*hit_probability
        return result

    def divided_result(self, target: Target, range_value:int) -> float:
        float_result = self.wound_count(target, range_value)/self.divider()
        return float(int(float_result*100))/100
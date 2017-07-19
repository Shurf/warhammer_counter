__author__ = 'schrecknetuser'
import typing
from .targets import Target

class Profile:
    def __init__(self, min_range:int, max_range:int, strength: int, ap:int, shots:float, damage:float):
        self.strength = strength
        self.min_range = min_range
        self.max_range = max_range
        self.ap = ap
        self.shots = shots
        self.damage = damage

dice_side_count = 6

class Weapon:

    def is_autohit(self):
        return False

    def is_reroll_wound(self):
        return False

    def hit_probability(self, ballistic_skill, overwatch:bool):
        if self.is_autohit():
            return 1.0
        if overwatch:
            return float(1)/6
        return float(dice_side_count + 1 - ballistic_skill)/dice_side_count


    def wound_probability(self, range_value: int, target: Target):
        strength = self.strength(range_value)
        toughness = target.toughness()
        value = 0
        if strength == 0:
            return 0
        if strength * 2 <= toughness:
            value = float(1) / 6
        elif strength < toughness:
            value = float(2) / 6
        elif strength == toughness:
            value = float(1) / 2
        elif strength >= toughness * 2:
            value = float(5) / 6
        elif strength > toughness:
            value = float(2) / 3

        if self.is_reroll_wound():
            value += (1 - value) * value

        return value

    def __init__(self, name:str, point_cost:int, profiles:typing.List[Profile]):
        self.name = name
        self.point_cost_value = point_cost
        self.profiles = profiles

    def profile(self, range):
        profile = next((x for x in self.profiles if x.min_range < range and x.max_range >= range), None)
        return profile

    def strength(self, range_value:int):
        profile = self.profile(range_value)
        if profile is None:
            return 0
        return profile.strength

    def ap(self, range_value:int) -> int:
        profile = self.profile(range_value)
        if profile is None:
            return 0
        return profile.ap

    def shots(self, range_value:int) -> float:
        profile = self.profile(range_value)
        if profile is None:
            return 0
        return profile.shots

    def damage(self, target:Target, range_value:int) -> float:
        profile = self.profile(range_value)
        if profile is None:
            return 0
        return profile.damage

    def point_cost(self):
        return self.point_cost_value

    def name(self):
        return self.name






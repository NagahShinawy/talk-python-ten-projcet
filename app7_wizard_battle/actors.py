"""
created by Nagaj at 13/05/2021
"""
import random

from constants import WIZARD_ATTACKS, HERO_ROLL, CREATURE_ROLL, TRIUMPHED, DEFEATED


class Base:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return f"<{self.__class__.__name__}>{self.name}-{self.level}"


class Creature(Base):
    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class SmallAnimal(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll / 2


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breaths_fire):
        super().__init__(name, level)
        self.scaliness = scaliness
        self.breaths_fire = breaths_fire

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        fire_modifier = 5 if self.breaths_fire else 1
        scale_modifier = self.scaliness / 10
        return base_roll * fire_modifier * scale_modifier


class Wizard(Creature):
    def attack(self, creature: Creature):
        print(WIZARD_ATTACKS.format(wizard_name=self.name, creature_name=creature.name))
        hero_roll = self.get_defensive_roll()
        creature_roll = creature.get_defensive_roll()

        print(HERO_ROLL.format(self.name, hero_roll))
        print(CREATURE_ROLL.format(creature.name, creature_roll))
        if hero_roll >= creature_roll:
            print(TRIUMPHED.format(creature.name))
            return True
        else:
            print(DEFEATED)
        return False

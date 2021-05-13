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
    pass


class Wizard(Base):

    def attack(self, creature: Creature):
        print(WIZARD_ATTACKS.format(wizard_name=self.name, creature_name=creature.name))
        hero_roll = random.randint(1, 12) * self.level
        creature_roll = random.randint(1, 12) * creature.level

        print(HERO_ROLL.format(self.name, hero_roll))
        print(CREATURE_ROLL.format(creature.name, creature_roll))
        if hero_roll >= creature_roll:
            print(TRIUMPHED.format(creature.name))
            return True
        else:
            print(DEFEATED)
        return False

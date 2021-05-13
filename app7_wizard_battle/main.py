"""
created by Nagaj at 13/05/2021
"""
import random
import time
from actors import Wizard, Creature
from app7_wizard_battle.constants import (
    EXIT,
    GOOD_BYE,
    ATTACK,
    RUN,
    LOOK,
    ACTIVE_CREATURE,
    KILL,
    RECOVER,
    RETURNS,
    WAIT,
    SEES,
    LIST,
    RUNAWAY,
    TIMES
)
from validations import validated_cmd
from art import print_header


def wizard_recovering():
    print(RECOVER.format(WAIT))
    time.sleep(WAIT)
    print(RETURNS)


def wizard_look(hero, creatures):
    print(SEES.format(hero.name))
    for counter, creature in enumerate(creatures, start=1):
        print(LIST.format(counter=counter, creaturename=creature.name, creaturelevel=creature.level))
    print("#" * TIMES)


def game_loop():
    creatures = [
        Creature("Toad", 1),
        Creature("Bat", 3),
        Creature("Dragon", 50),
        Creature("Evil Wizard", 1000),
    ]
    hero = Wizard("GandOlf", 75)
    while True:
        if not creatures:
            print(KILL)
            break
        active_creature = random.choice(creatures)
        print(
            ACTIVE_CREATURE.format(
                name=active_creature.name, level=active_creature.level
            )
        )
        cmd = validated_cmd()
        if cmd == ATTACK:
            if hero.attack(active_creature) and len(creatures) > 0:
                creatures.remove(active_creature)
            else:
                wizard_recovering()
        elif cmd == RUN:
            print(RUNAWAY)

        elif cmd == LOOK:
            wizard_look(hero, creatures)

        elif cmd == EXIT:
            print(GOOD_BYE)
            break


def main():
    print_header()
    game_loop()


if __name__ == "__main__":
    main()

from gameplay.green_die import GreenDie
from gameplay.red_die import RedDie
from models.geometry import get_arc_footprint, get_range_footprint

class Combat:
    """
    This class represents the Combat phase of a turn
    """
    def __init__(self, game):
        """
        Constructor
        game: The game under way
        """
        self._game = game

    def execute(self):
        """
        Run the Combat phase
        """
        for pilot in self._game.pilots_by_skill(ascending=False):
            pilot.active = True
            self._attack(pilot)
            pilot.active = False

    def _attack(self, pilot):
        """
        Carry out the Attack phase of combat for the given pilot
        pilot: The pilot to attack with
        """
        player = self._game.player(pilot.faction)

        # Choose weapon
        weapon_options = pilot.weapon_options()
        if not weapon_options:
            print("Pilot {0} has no weapons to attack with")
        else:
            if len(weapon_options) > 1:
                chosen_weapon = player.choose_attack_weapon(pilot, weapon_options)
            else:
                chosen_weapon = weapon_options[0]

            # Declare target
            target_options, footprint = self._get_target_options(pilot, chosen_weapon)
            if not target_options:
                print("Pilot {0} has no enemies in range to attack with weapon {1}".format(pilot.name, chosen_weapon.name))
            else:
                self._game.board.footprints = [footprint]
                chosen_target = player.choose_attack_target(pilot, target_options)
                self._game.board.footprints = []
                if chosen_target:
                    # Attack this target with the chosen weapon
                    self._begin_attack(pilot, chosen_target, chosen_weapon)

    def _get_target_options(self, pilot, weapon):
        """
        Get the list of enemies that can be targeted by this pilot
        pilot: The pilot to attack with
        weapon: The weapon to attack with
        return: ([pilots who can be attacked], footprint geometry)
        """
        footprint = get_range_footprint(pilot.ship.get_base_shape(), weapon.ranges)
        if weapon.firing_arc < 360:
            # Not a turret - our range footprint needs to be within arc as well
            arc_footprint = get_arc_footprint(pilot.ship, weapon)
            footprint = footprint.intersection(arc_footprint)

        other_player_pilots = self._game.other_player(pilot.faction).pilots()
        target_options = [target_pilot for target_pilot in other_player_pilots if footprint.intersects(target_pilot.ship.get_base_shape())]
        return target_options, footprint

    def _begin_attack(self, pilot, target, weapon):
        """
        Begin the attack
        pilot: The pilot doing the attacking
        target: The pilot being attacked
        weapon: The weapon being used to attack with
        """
        # TODO
        attack_range = 3

        # Roll red dice
        print("{0} is attacking {1} with its {2} weapon at range {3}".format(pilot.name, target.name, weapon.name, attack_range))
        attack_strength = pilot.attack + pilot.attack_bonus(attack_range)
        red_dice = [RedDie.roll() for die_index in range(attack_strength)]
        print("Red dice results: {0}".format(", ".join(red_dice)))

        # Roll green dice
        defence_strength = target.agility + target.agility_bonus(attack_range)
        green_dice = [GreenDie.roll() for die_index in range(defence_strength)]
        print("Green dice results: {0}".format(", ".join(green_dice)))

        # Cancel red dice with green dice: damage first, then crits
        evades = sum([1 if die == GreenDie.EVADE else 0 for die in green_dice])
        final_red_dice = []
        for die in red_dice:
            if die == RedDie.DAMAGE:
                if evades > 0:
                    evades -= 1
                else:
                    final_red_dice.append(die)
        for die in red_dice:
            if die == RedDie.CRIT:
                if evades > 0:
                    evades -= 1
                else:
                    final_red_dice.append(die)

        # Deal damage!
        damage_count = sum([1 if die == RedDie.DAMAGE else 0 for die in final_red_dice])
        crit_count = sum([1 if die == RedDie.CRIT else 0 for die in final_red_dice])
        for index in range(damage_count):
            if target.shield > 0:
                target.shield -= 1
            else:
                target.damage_cards.append(self._game.damage_cards.pop())
        for index in range(crit_count):
            if target.shield > 0:
                target.shield -= 1
            else:
                target.damage_cards.append(self._game.damage_cards.pop())
                target.damage_cards[-1].flip_faceup()

        if target.is_alive():
            print("{0} dealt {1} damage and {2} crits to {3} [now has {4}/{5} shield and {6}/{7} damage]".format(
                pilot.name,
                damage_count,
                crit_count,
                target.name,
                target.shield,
                target.max_shield,
                target.damage_count(),
                target.hull))
        else:
            print("{0} has killed {1} with {2} damage and {3} crits!".format(pilot.name, target.name, damage_count, crit_count))
            self._game.board.pilots.remove(target)
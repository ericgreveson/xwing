import random

class Combat:
    """
    This class represents the Combat phase of a turn
    """
    PRIMARY_WEAPON = "primary"

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

        # Declare target
        target_options = self._get_target_options(pilot)
        if not target_options:
            print("Pilot {0} has no enemies in range to attack".format(pilot.name))
        else:
            chosen_target = player.choose_attack_target(pilot, target_options)
            if chosen_target:
                # Choose weapon, if options exist
                # TODO: I know that the order in the rules is "choose weapon, choose target" but since
                # you're allowed to measure range and arc before either of these, this order seems easier.
                weapon_options = self._get_weapon_options(pilot, chosen_target)
                if not weapon_options:
                    print("Pilot {0} has no weapons to attack with")
                else:
                    if len(weapon_options) > 1:
                        chosen_weapon = player.choose_attack_weapon(pilot, chosen_target, weapon_options)
                    else:
                        chosen_weapon = weapon_options[0]

                    # Attack this target with the chosen weapon
                    self._roll_attack_dice(pilot, chosen_target, chosen_weapon)

    def _get_target_options(self, pilot):
        """
        Get the list of enemies that can be targeted by this pilot
        pilot: The pilot to attack with
        return: List of pilots who can be attacked
        """
        target_options = []
        return target_options

    def _get_weapon_options(self, pilot, target):
        """
        Get the list of weapons that can be used by pilot to attack target
        pilot: The pilot to attack with
        target: The pilot being attacked
        return: List of weapon options to attack with (upgrades or PRIMARY_WEAPON)
        """
        weapon_options = [Combat.PRIMARY_WEAPON]
        return weapon_options

    def _roll_attack_dice(self, pilot, target, weapon):
        """
        Begin the attack
        pilot: The pilot doing the attacking
        target: The pilot being attacked
        weapon: The weapon being used to attack with
        """
        print("{0} is attacking {1} with its {2} weapon".format(pilot.name, target.name, weapon))
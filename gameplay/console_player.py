from actions.action_registry import ActionRegistry
from gameplay.player import Player
from models.bearing_registry import BearingRegistry
from models.faction import Faction

import os

class ConsolePlayer(Player):
    """
    This class represents a player who uses the console to enter commands
    """
    DEFAULT_SQUAD_LIST = {
        Faction.rebel: os.path.join("data", "example_rebel_squad.xws.json"),
        Faction.imperial: os.path.join("data", "example_imperial_squad.xws.json")
        }
    DEFAULT_SQUAD_SETUP = {
        Faction.rebel: os.path.join("data", "example_rebel_squad.setup.json"),
        Faction.imperial: os.path.join("data", "example_imperial_squad.setup.json")
        }

    def __init__(self, faction, board):
        """
        Constructor
        faction: The faction that this player is playing as
        board: The game board
        """
        super().__init__(faction, board)

    def choose_squad_list(self):
        """
        Return an XWS file path representing your squad list
        """
        # For now, we'll load this from file
        return self._get_file_name(
            "Enter path to squad list XWS file:",
            default=ConsolePlayer.DEFAULT_SQUAD_LIST[self.faction])

    def choose_initiative(self):
        """
        Return True if you want initiative, False if your opponent should have it
        """
        return self._get_answer("Do you want initiative?", ["y", "n"]) == "y"

    def choose_squad_setup(self):
        """
        Return a .setup.json file path representing your squad setup
        """
        return self._get_file_name(
            "Enter path to squad setup JSON file:",
            default=ConsolePlayer.DEFAULT_SQUAD_SETUP[self.faction])

    def choose_dial(self, pilot):
        """
        Return a Maneuver from the given pilot's ship's dial
        """
        bearing_names = [maneuver.named_bearing().name for maneuver in pilot.ship.dial.maneuvers()]
        print("Green: {0}".format(", ".join([bearing.name for bearing in pilot.ship.dial.green])))
        print("White: {0}".format(", ".join([bearing.name for bearing in pilot.ship.dial.white])))
        print("Red:   {0}".format(", ".join([bearing.name for bearing in pilot.ship.dial.red])))
        bearing_name = self._get_answer("Choose bearing for {0}:".format(pilot.name), bearing_names, show_options=False)
        chosen_named_bearing = BearingRegistry.named_bearing_from_string(bearing_name)
        return pilot.ship.dial.maneuver_from_named_bearing(chosen_named_bearing)
    
    def choose_action(self, pilot):
        """
        Return an action from the given pilot's available_actions(), or None if no action requested
        """
        action_names = [action.__name__ for action in pilot.available_actions()]
        if not action_names:
            return None

        action_names += ["None"]
        action_name = self._get_answer("Choose action for {0}:".format(pilot.name), action_names)
        if action_name == "None":
            return None
        else:
            # TODO: allow for selecting parameters other than the pilot, e.g. target locks and barrel roll/boost direction
            # Maybe in separate calls when action is executed, in case chosen action is invalid and they need to select again?
            action_class = ActionRegistry.action_class_from_string(action_name)
            return action_class()
        
    def choose_attack_target(self, pilot, target_options):
        """
        Return a target from the available targets, or None if no attack requested
        pilot: The pilot doing the attacking
        target_options: List of enemy pilots who are in range of at least one weapon
        """
        print("0: None")
        for target_index, target in enumerate(target_options):
            print("{0}: {1}".format(target_index + 1, target.name))
        chosen_index = int(self._get_answer("Choose target for {0}".format(pilot.name), [str(i) for i in range(len(target_options) + 1)]))
        if chosen_index == 0:
            return None
        else:
            return target_options[chosen_index - 1]

    def choose_attack_weapon(self, pilot, target, weapon_options):
        """
        Return a weapon to attack the given target with out of the available options
        pilot: The pilot doing the attacking
        target: The enemy pilot being attacked
        weapon_options: The list of weapons that can be chosen
        """
        raise NotImplementedError()

    def _get_answer(self, question_text, valid_responses, show_options=True):
        """
        Ask a question on the console. Keep asking until we get a sensible answer.
        question_text: Question text to display
        valid_responses: List of strings containing valid responses
        show_options: If true, append the options list to the displayed question
        return: the selected string from valid_responses
        """
        self._show_faction()
        display_string = question_text + " "
        options_text = "[{0}]".format(", ".join(valid_responses))
        if show_options:
            display_string += options_text + " "

        while True:
            response = input(display_string)
            if response not in valid_responses:
                print("  Try again. Valid responses: {0}".format(options_text))
            else:
                return response

    def _get_file_name(self, question_text, default=None, require_exists=True):
        """
        Ask for a file name on the console
        question_text: Question text to display
        default: If supplied, hitting Enter will select this file
        require_exists: If True, keep asking until an existing file is selected
        return: Full path to file
        """
        self._show_faction()
        display_string = question_text + " "
        if default:
            display_string += "[default: {0}] ".format(default)
        while True:
            response = input(display_string)
            if default and not response:
                response = default
            if not require_exists or os.path.exists(response):
                return response

            print("File '{0}' doesn't exist: please try again.".format(response))

    def _show_faction(self):
        """
        Print the current player's faction
        """
        print("({0} player)".format(self.faction.name.capitalize()))
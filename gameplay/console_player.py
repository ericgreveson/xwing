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
        Return a Bearing from the given pilot's ship's dial
        """
        bearing_names = [bearing.name for bearing, difficulty in pilot.ship.dial.bearings()]
        print("Green: {0}".format(", ".join([bearing.name for bearing in pilot.ship.dial.green])))
        print("White: {0}".format(", ".join([bearing.name for bearing in pilot.ship.dial.white])))
        print("Red:   {0}".format(", ".join([bearing.name for bearing in pilot.ship.dial.red])))
        bearing_name = self._get_answer("Choose bearing for {0}:".format(pilot.name), bearing_names, show_options=False)
        return BearingRegistry.bearing_from_string(bearing_name)

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
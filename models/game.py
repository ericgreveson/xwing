from models.damage_card import DamageCard

import functools

class Game:
    """
    Model for a complete X-Wing game
    """
    def __init__(self, board, players, pilot_registry):
        """
        Constructor
        board: The game board representing the game state
        players: The list (of length two) of players
        pilot_registry: The pilot registry
        """
        self.board = board
        self.players = players
        self.pilot_registry = pilot_registry

        # TODO: fix up to be real damage cards
        self.damage_cards = [DamageCard() for index in range(32)]

    def player(self, faction):
        """
        Get the player for the given faction
        faction: The faction to get the player for
        return: The player of the given faction
        """
        for player in self.players:
            if player.faction == faction:
                return player

        raise ValueError("Given faction is not playing!")

    def other_player(self, faction):
        """
        Get the player that isn't the given faction
        faction: The faction of player A
        return: The player that isn't player A (i.e. player B)
        """
        for player in self.players:
            if player.faction != faction:
                return player
    
    def is_over(self):
        """
        Is the game over?
        """
        return not all([player.is_alive() for player in self.players])

    def pilots_by_skill(self, ascending = True):
        """
        Get list of all pilots, sorted by activation order
        ascending: If True, sort in ascending order (e.g. Activation), otherwise descending (e.g. Combat)
        return: List of pilots, with skill ties broken by initiative first
        """
        return sorted(self.board.pilots,
                      key=functools.partial(self._skill_sort_key, initiative_multiplier = 1 if ascending else -1),
                      reverse=not ascending)

    def _skill_sort_key(self, pilot, initiative_multiplier):
        """
        Generate a numeric key for sorting pilots in activation order
        pilot: The pilot to generate the key for
        initiative_multiplier: The initiative bonus multiplier (1 for Activation order, -1 for Combat order)
        """
        skill_bonus = 0 if self.player(pilot.faction).has_initiative else 0.5
        return pilot.skill + initiative_multiplier * skill_bonus
from actions.barrel_roll import BarrelRoll
from actions.boost import Boost
from actions.evade import Evade
from actions.focus import Focus
from actions.target_lock import TargetLock

class ActionRegistry:
    """
    This represents all actions
    """
    ACTIONS = [BarrelRoll, Boost, Evade, Focus, TargetLock]

    @staticmethod
    def action_class_from_string(action_name):
        """
        Get an action class from its string name
        """
        for action in ActionRegistry.ACTIONS:
            if action.__name__ == action_name:
                return action

        raise ValueError("Unknown action: {0}".format(action_name))
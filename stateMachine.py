"""
    ############################################################
    We define the state machine.
"""

from states import MainState

"""
    ############################################################
    A simple state machine
"""


class StateMachine(object):

    next_state_data = "null-action", "null-object", "null-tag"

    def __init__(self):
        """
        Initialize the components.
        """

        # Start with a default state.
        self.state = MainState()

    def event(self, event):
        """
        Incoming chats are delegated to the given states which then handle the event. The result is
        then assigned as the new state. resulting chat out is returned.
        """

        # The next state will be the result of the on_event function.
        next_state, self.next_state_data = self.state.event(event, self.next_state_data)
        chat_out = self.state.chat_out
        self.state = next_state
        return chat_out

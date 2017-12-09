"""
    ############################################################
    Define a state object with general utility functions for the
    individual states.
"""


class State(object):

    chat_out = "This is the default chat out for state object"

    def __init__(self):
        print('Processing current state:', str(self))

    def event(self, read_in):
        """
        Handle events that are delegated to this State.
        """
        pass

    def __repr__(self):
        """
        Leverages the __str__ method to describe the State.
        """
        return self.__str__()

    def __str__(self):
        """
        Returns the name of the State.
        """
        return self.__class__.__name__
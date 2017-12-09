"""
    ############################################################
    chatbot
"""

from generalFunctions import make_lower
from stateMachine import StateMachine


"""
    ############################################################
    initiate chatbot
"""


class Chatbot(object):

    SM = StateMachine()

    def run(self, chat_in):
        chat_out = self.SM.event(make_lower(chat_in))
        return chat_out

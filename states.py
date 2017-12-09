"""
    ############################################################
    We define states based on the state object with unique functionality
"""

from stateObject import State
from chatEngine import run_chat_engine
from questionFeedbackEngine import run_question_feedback_engine
from confirmUpdateUserDataEngine import run_confirm_update_user_data_engine
from updateUserDataEngine import run_update_user_data_engine
from alarmEngine import run_alarm_engine
from updateAlarmEngine import run_update_alarm_engine
"""
    ############################################################
    Main state contain all the basic chat functionality.
"""


class MainState(State):

    chat_out = "This is the default chat out for MainState"

    def event(self, chat_in, next_state_data):
        self.chat_out, next_sate_id, next_state_data = run_chat_engine(chat_in, next_state_data)
        if next_sate_id == 0:
            return MainState(), next_state_data
        elif next_sate_id == 1:
            return QuestionFeedbackState(), next_state_data
        elif next_sate_id == 2:
            return ConfirmUpdateUserDataState(), next_state_data
        elif next_sate_id == 3:
            return UpdateUserDataState(), next_state_data
        elif next_sate_id == 4:
            return AlarmState(), next_state_data
        elif next_sate_id == 5:
            return UpdateAlarmState(), next_state_data
        else:
            return self


"""
    ############################################################
    Requiring a feedback for a question
"""


class QuestionFeedbackState(State):

    chat_out = "This is the default chat out for QuestionFeedbackState"

    def event(self, chat_in, next_state_data):
        self.chat_out, next_sate_id, next_state_data = run_question_feedback_engine(chat_in, next_state_data)
        if next_sate_id == 0:
            return MainState(), next_state_data
        elif next_sate_id == 1:
            return QuestionFeedbackState(), next_state_data
        elif next_sate_id == 2:
            return ConfirmUpdateUserDataState(), next_state_data
        elif next_sate_id == 3:
            return UpdateUserDataState(), next_state_data
        elif next_sate_id == 4:
            return AlarmState(), next_state_data
        elif next_sate_id == 5:
            return UpdateAlarmState(), next_state_data
        else:
            return self


"""
    ############################################################
    Requiring to confirm to initiate the update
"""


class ConfirmUpdateUserDataState(State):

    chat_out = "This is the default chat out for ConfirmUpdateUserDataState"

    def event(self, chat_in, next_state_data):
        self.chat_out, next_sate_id, next_state_data = run_confirm_update_user_data_engine(chat_in, next_state_data)
        if next_sate_id == 0:
            return MainState(), next_state_data
        elif next_sate_id == 1:
            return QuestionFeedbackState(), next_state_data
        elif next_sate_id == 2:
            return ConfirmUpdateUserDataState(), next_state_data
        elif next_sate_id == 3:
            return UpdateUserDataState(), next_state_data
        elif next_sate_id == 4:
            return AlarmState(), next_state_data
        elif next_sate_id == 5:
            return UpdateAlarmState(), next_state_data
        else:
            return self


"""
    ############################################################
    Update user data
"""


class UpdateUserDataState(State):

    chat_out = "This is the default chat out for UpdateUserDataState"

    def event(self, chat_in, next_state_data):
        self.chat_out, next_sate_id, next_state_data = run_update_user_data_engine(chat_in, next_state_data)
        if next_sate_id == 0:
            return MainState(), next_state_data
        elif next_sate_id == 1:
            return QuestionFeedbackState(), next_state_data
        elif next_sate_id == 2:
            return ConfirmUpdateUserDataState(), next_state_data
        elif next_sate_id == 3:
            return UpdateUserDataState(), next_state_data
        elif next_sate_id == 4:
            return AlarmState(), next_state_data
        elif next_sate_id == 5:
            return UpdateAlarmState(), next_state_data
        else:
            return self


"""
    ############################################################
    Alarm
"""


class AlarmState(State):

    chat_out = "This is the default chat out for Alarm state"

    def event(self, chat_in, next_state_data):
        self.chat_out, next_sate_id, next_state_data = run_alarm_engine(chat_in, next_state_data)
        if next_sate_id == 0:
            return MainState(), next_state_data
        elif next_sate_id == 1:
            return QuestionFeedbackState(), next_state_data
        elif next_sate_id == 2:
            return ConfirmUpdateUserDataState(), next_state_data
        elif next_sate_id == 3:
            return UpdateUserDataState(), next_state_data
        elif next_sate_id == 4:
            return AlarmState(), next_state_data
        elif next_sate_id == 5:
            return UpdateAlarmState(), next_state_data
        else:
            return self


"""
    ############################################################
    Update Alarm
"""


class UpdateAlarmState(State):

    chat_out = "This is the default chat out for UpdateAlarmState"

    def event(self, chat_in, next_state_data):
        self.chat_out, next_sate_id, next_state_data = run_update_alarm_engine(chat_in, next_state_data)
        if next_sate_id == 0:
            return MainState(), next_state_data
        elif next_sate_id == 1:
            return QuestionFeedbackState(), next_state_data
        elif next_sate_id == 2:
            return ConfirmUpdateUserDataState(), next_state_data
        elif next_sate_id == 3:
            return UpdateUserDataState(), next_state_data
        elif next_sate_id == 4:
            return AlarmState(), next_state_data
        elif next_sate_id == 5:
            return UpdateAlarmState(), next_state_data
        else:
            return self

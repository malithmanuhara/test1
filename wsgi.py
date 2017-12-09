import atexit
import datetime
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from chatbot import Chatbot
from generalFunctions import flash_string
from reminderBot import reminder_bot
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger


"""
    ############################################################
    App config.
"""
DEBUG = True
application = Flask(__name__)
application.config.from_object(__name__)
application.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


"""
    ############################################################
    Print Date Time
"""

print(datetime.datetime.now())


class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])

"""
    ############################################################
    Instantiate Chatbot
"""

CB = Chatbot()

"""
    START ############################################################
"""
flash_str = ["null_txt", 0]


def run_alarm():
    global flash_str
    alarm_string = reminder_bot()
    if alarm_string != "no-alarm":
        flash_str = [alarm_string, 1]
    print("flash_string : " + flash_str[0])

scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(
    func=run_alarm,
    trigger=IntervalTrigger(seconds=5),
    id='reminder_job',
    name='check for reminders every five seconds',
    replace_existing=True)
# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())

"""
    END ############################################################
"""

"""
    ############################################################
    Web interface routing
"""


@application.route("/", methods=['GET', 'POST'])
def chatbot_interface():

    """
    ########################################
    """

    global flash_str

    if flash_str[1] == 1:
        flash_string(flash_str[0])
        flash_str[1] = 0

    """
        ########################################
    """

    form = ReusableForm(request.form)
    print(form.errors)
    if request.method == 'POST':
        chat_in = request.form['name']
        print(chat_in)

        chat_out = CB.run(chat_in)
        print(chat_out)

        if form.validate():
            # Save the comment here.
            flash_string(chat_out)
        else:
            flash('Error: Empty text field. ')

    return render_template('chatbot_interface.html', form=form)


if __name__ == "__main__":
    application.run()

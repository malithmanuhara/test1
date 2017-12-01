from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from threading import Thread
from remindBot import remind_bot
from respondGenerator import respond_generator



# App config.
DEBUG = True
application = Flask(__name__)
application.config.from_object(__name__)
application.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])


thread_remind = Thread(target=remind_bot)
thread_remind.start()


@application.route("/", methods=['GET', 'POST'])
def chatbot_interface():

    raw = "NULL"
    # chat loop
    form = ReusableForm(request.form)
    print(form.errors)
    if request.method == 'POST':
        chat_in = request.form['name']
        print(chat_in)
        chat_out = respond_generator(chat_in)

        if form.validate():
            # Save the comment here.
            flash(chat_out)
        else:
            flash('Error: Empty text field. ')

    return render_template('chatbot_interface.html', form=form)


def flash_string(string):
    flash(string)

if __name__ == "__main__":
    application.run()

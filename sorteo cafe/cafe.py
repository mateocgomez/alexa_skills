from flask import Flask, render_template
from flask_ask import Ask, statement, question

app = Flask(__name__)
ask = Ask(app, '/')

# here we are trying to get the text fetched from them user it self to change the welcome text you just need to change it in .json file and done
@ask.launch
def launch():
    welcome_text = render_template('welcome_text')
    return question(welcome_text)

# the default fall back intent for Amazon Alexa 

@ask.intent('AMAZON.FallbackIntent')
def fallback():
    reprompt_text = render_template('ask_name_reprompt')
    return question(rempromt_text)

# the main intent that can be used to call the welcome msg 
@ask.intent('CafeIntent')
def hello(firstname):
    if firstname is None:
        #Si ningun nombre ha sido enviado
        # ask for name
        ask_name_text = render_template('ask_name')
        return question(ask_name_text)
    # render template is used to set an response. 
    response_text = render_template('hello', firstname=firstname)
    return statement(response_text).simple_card('Hola', response_text)

if __name__ == '__main__':
    app.run(debug=True)

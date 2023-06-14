from flask import *
from bardapi import Bard
import os
from script import engScript, hinScript
from words import word, word1, definition, definition1
from tips import random_tip

os.environ["_BARD_API_KEY"] = os.getenv('API_KEY')

app = Flask(__name__)

@app.route('/')
def index():
    msg=hinScript
    r_t = random_tip
    return render_template('index.html', translated=msg, tip = r_t)


@app.route('/search', methods=['POST'])
def result():
    # getting input from html page
    text = request.form['msg']
    userInput = '{}'.format(text)

    msg = f"compare this sentence '{userInput}' with '{engScript}' and find the areas in which the sentence is wrong with respect to second sentence. Tell in 1-2 lines, reply in only plain text"

    aiMsg = Bard().get_answer(str(msg))['content']

    #initliasing words
    r_word = word
    r_word1 = word1

    r_def = definition
    r_def1 = definition1

    return render_template('result.html', userInput=userInput, aiMsg=aiMsg, random_script=engScript, word = r_word, word1 = r_word1, define = r_def, define1 = r_def1)



if __name__ == '__main__':
    app.run(debug=True)

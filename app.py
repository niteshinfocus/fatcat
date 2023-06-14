from flask import *
import openai
import os
from script import engScript, hinScript
from words import word, word1, definition, definition1
from tips import random_tip

openai.api_key = os.getenv('OPENAI_API_KEY')

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

    #generating response
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "compare this sentence '" + userInput +" '" + " with '" + engScript + " ' "+ " and find the areas in which the sentence is wrong with respect to second sentence. Tell in 2-3 lines"}])
    aiMsg = completion.choices[0].message.content

    #initliasing words
    r_word = word
    r_word1 = word1

    r_def = definition
    r_def1 = definition1

    return render_template('result.html', userInput=userInput, aiMsg=aiMsg, random_script=engScript, word = r_word, word1 = r_word1, define = r_def, define1 = r_def1)



if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request
from Code.dictionary_words import *
from random import randint
from Code.listogram import *

app = Flask(__name__, template_folder='Templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result')
def show_results():
    listogram = Listogram(["apple", "pear", "strawberry", "orange", "mango", "banana"])
    random_word = listogram.sample()
    return render_template('results.html', random_word=random_word)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))

from flask import Flask, render_template, request
from Code.dictionary_words import *
from random import randint
from Code.listogram import *
from Code.markov_chain import *
from TwitterAPI import TwitterAPI

app = Flask(__name__, template_folder='Templates')
#
# api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result')
def show_results():
    tweet = markov()
    print(tweet)
    return render_template('results.html', tweet=tweet)

@app.route('/tweet', methods=['POST', 'GET'])
def tweet():
    r = api.request('statuses/update', {'status':{{tweet}}})
    if r.status_code == 200:
        print("Success!")
    else:
        print("FAILURE!")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))

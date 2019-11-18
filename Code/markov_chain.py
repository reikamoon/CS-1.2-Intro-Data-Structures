from dictogram import Dictogram
from random import choice

def markov_chain(word_list):
    markov = {}
    for i in range(len(word_list)):
        if word_list[i] not in markov:
            markov[word_list[i]] = []
        if i < len(word_list) - 1:
            markov[word_list[i]].append(word_list[i + 1])

    for key in markov:
        markov[key] = Dictogram(markov[key])

    return markov

def random_walk(chain, length):
    output = []
    output.append(choice(tuple(chain.keys())))
    for i in range (length):
        output.append(chain[output[i]].sample())

    string = ""
    for word in output:
        string += word + " "

    return string

def sentence():
    text = 'one fish two fish red fish blue fish'
    print(random_walk(markov_chain(text),10))

if __name__ == '__main__':
    sentence()

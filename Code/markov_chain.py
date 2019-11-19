from dictogram import *
from histograms import *
from random import choice

class Markov():
    def __init__(self, word_file):
        self.word_list = read_file(word_file)
        self.markov = self.make_chain(self.word_list)

    def make_chain(self, word_list):
        markov = {}
        for i in range(len(word_list)):
            if word_list[i] not in markov:
                markov[word_list[i]] = []
            if i < len(word_list) -1:
                markov[word_list[i]].append(word_list[i + 1])

        for key in markov:
            markov[key] = Dictogram(markov[key])

        return markov

    def walk(self, length):
        output = []
        output.append(choice(tuple(self.markov.keys())))
        for i in range(length):
            output.append(self.markov[output[i]].sample())

        string = ""
        for word in output:
            string += word + " "
        return string

def markov(num):
    markov = Markov('Code/markov.txt')
    return markov.walk(num)

if __name__ == '__main__':
    markov(5)
    print(markov(5))

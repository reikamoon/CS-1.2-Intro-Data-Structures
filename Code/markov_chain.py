from Code.dictogram import *
from Code.histograms import *
from Code.queue import *
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

def markov():
    markov = MarkovChainHigher('Code/corpus.txt', 3)
    return markov.walk()

class MarkovChainHigher():
    def __init__(self, word_file, n):
        self.word_list = read_file(word_file)
        self.n = n
        self.markov = self.make_chain(self.word_list)

    def make_chain(self, word_list):
        queue = Queue()
        markov = {}
        n = self.n
        if queue.length() == 0:
            for i in range(n):
                queue.enqueue(word_list[i])
        for words in word_list:
            key = str(queue)
            queue.enqueue(words)
            queue.dequeue()

            if key not in markov:
                markov[key] = []
            markov[key].append(str(queue))

        for key in markov:
            markov[key] = Dictogram(markov[key])

        return markov

    def walk(self):
        output = []
        output.append(choice(tuple(self.markov.keys())))
        while output[0][0].islower():
            output[0] = choice(tuple(self.markov.keys()))
        i = 0
        while output[-1][-1] != ".":
            output.append(self.markov[output[i]].sample())
            i += 1


        string = ""
        for word in output:
            if output.index(word) == 0:
                string += word + " "
            else:
                string += word.split()[-1] + " "
        return string




if __name__ == '__main__':
    markov()
    print(markov())

from random import randint
from os import sys

def get_words():
    words = list()
    with open('/usr/share/dict/words', 'r') as f:
        words = f.read().split('\n')
    return words

def random_words(integer_input, word_list):
    sentence = str()
    while integer_input > 0:
        index = randint(0, len(words) - 1)

        if integer_input == 1:
            print("My Random Sentence:")
        else:
            sentence += word_list[index] + ' '

        integer_input -= 1
    return sentence

if __name__ == '__main__':
    words = get_words()
    integer_input = int(sys.argv[1])
    print(random_words(integer_input, words))

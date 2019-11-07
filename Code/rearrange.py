from os import sys
import random
from collections import defaultdict

#Rearrange a string given in the terminal
def rearrange(arguments):
    length = len(arguments)
    output = ""
    while length > 0:
        rerranger = random.randint(0, length - 1)
        output += arguments.pop(rerranger) + " "
        length -= 1
    return output

#Fisher Yates Shuffle
def fisher_yates_shuffle(obj):
    if obj == str(obj):
        string = True
    else:
        string = False

    obj = list(obj)
    num = len(obj)

    while num:
        num -= 1
        random = randint(0, num)
        hold = obj[num]
        obj[num] = obj[random]
        obj[random] = hold

    if string:
        obj = ''.join(obj)
    return obj

def shuffle(arguments):
    fisher_yates_shuffle(arguments)
    return arguments

#Reverse!
def reverse(arguments):
    str=arguments
    slicedString=str[stringlength :: -1]
    return(slicedString)

if __name__ == '__main__':
    arguments = sys.argv[1:]
    input = sys.argv
    word_source = load_anagram_words()
    print_anagrams(word_source)

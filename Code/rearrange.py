from os import sys
import random
import textwrap

#Rearrange a string given in the terminal
def rearrange(arguments):
    length = len(arguments)
    output = ""
    while length > 0:
        rerranger = random.randint(0, length - 1)
        output += arguments.pop(rerranger) + " "
        length -= 1
    return output

#Reverse!
def reverse(arguments):
    str=arguments
    slicedString=str[stringlength :: -1]
    return(slicedString)

#Anagrams
def anagram(arguments):
    arguments = word
    if len(word) < 2:
        return word
    else:
        tmp = []
        for i, letter in enumerate(word):
            for j in anagrams(word[:i]+word[i+1]):
                tmp.append(j+letter)
    return tmp

if __name__ == '__main__':
    arguments = sys.argv[1:]
    input = sys.argv
    output = anagram(arguments)
    print anagram(input)

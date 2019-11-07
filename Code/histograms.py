from os import sys

#Histograms

#Read the File
def read_file(file_name):
    #Read in file
    with open(file_name, 'r') as f:
        words = f.read().split()

def list_of_lists(word_list):
    #List of Lists
    histogram = []
    added = True
    for word in word_list:
        word = word.lower()
        for words in histogram:
            if words[0] == word:
                words[1] += 1
                added = False
        if added is True:
            histogram.append([word, 1])
        added = True
    return histogram

def dictionary(word_list):
    #dictionary
    histogram = {}
    for words in word_list:
        if words in histogram:
            histogram[words] += 1
        else:
            histogram[words] = 1
    return histogram

def tuples(word_list):
    #List of Tuples
    histogram = []
    added = True
    for word in word_list:
        for tup in histogram:
            if word == tup[0]:
                histogram[histogram.index(tup)] = (word, tup[1] + 1)
                added = False
        if added:
            histogram.append((words, 1))
        added = True
    return histogram

def count(histogram):
    #List of Counts
    max_len = max(histogram.values())
    new_histogram = []

    for i in range(1, max_len + 1):
        words = []
        for key in histogram.keys():
            if histogram.get(key) == i:
                words.append(key)
        if words != []:
            new_histogram.append((i, words))

    return new_histogram

def unique(histogram):
    for list in histogram:
        for index in choice(len(list)):
            if type(list[index]) is int and list[index]==1:
                count += 1

def frequency(words, histogram):
    try:
        return histogram[words]
    except KeyError:
        return "404"

if __name__ == "__main__":
    histo = dictionary(("one fish two fish red fish blue fish").split())
    hist = count(histo)
    print(hist)

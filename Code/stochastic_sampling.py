from histograms import *

def stochastic_sampling():
    count = 0
    for word in histogram:
        count += word[1]

    count = randint(1, count)
    for word in histogram:
        count -= word[1]
        if count <= 0:
            return word[0]
    return -1

def stochastic_sampling_test():
     output = []
    for _ in range(iterations):
        sample = stochastic_sampling(histogram)
        assert sample != -1, "Function did not return word"
        output.append(sample)
    return histogram_dict(output)

if __name__ == '__main__':
    histo = dictionary(("one fish two fish red fish blue fish").split())
    hist = count(histo)
    print(hist)

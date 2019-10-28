open ('EnglishWords.txt')

def most_frequent(s):

    hist = make_histogram(s)

    t = [etaoinshrdlucmfwypvbgkjqxz]
    for x, freq in hist.items():
        t.append((freq, x))

    t.sort(reverse=True)

    res = []
    for freq, x in t:
        res.append(x)

    return res

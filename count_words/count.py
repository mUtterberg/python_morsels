from collections import Counter

PUNCTUATIONS = '!"#$%&()*+,-./:;<=>?@[\\]^_{|}~¿'

def count_words_in(text):
    for char in PUNCTUATIONS:
        text = text.replace(char, ' ')
    text = text.lower().split()

    return Counter(text)


def count_words(input_str):
    ''' Returns a dictionary with counts of each word in a string '''
    words = input_str.split(' ')
    slimwords = []
    worddict = {}
    for word in words:
        if word not in slimwords:
            slimwords.append(word)
    for word in slimwords:
        worddict[word] = words.count(word)
    return worddict

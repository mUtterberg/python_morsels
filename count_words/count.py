import string


def count_words(input_str):
    ''' Returns a dictionary with counts of each word in a string '''
    transformted_str = input_str.lower()
    words = transformted_str.split(' ')
    slimwords = []
    worddict = {}
    for ix in range(len(words)):
        while words[ix][0] not in string.ascii_lowercase:
            words[ix] = words[ix][1:]
        while words[ix][-1] not in string.ascii_lowercase:
            words[ix] = words[ix][:-1]
        if words[ix] not in slimwords:
            slimwords.append(words[ix])
    for word in slimwords:
        worddict[word] = words.count(word)
    return worddict

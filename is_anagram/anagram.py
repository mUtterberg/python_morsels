from unicodedata import normalize


def is_anagram(str_1, str_2):
    str_1 = normalize('NFD', str_1.lower())
    str_2 = normalize('NFD', str_2.lower())
    for letter in ''.join(x for x in (str_1+str_2).replace(' ', '') if x.isalpha()):
        str_1_count = str_1.count(letter)
        str_2_count = str_2.count(letter)
        if str_1_count != str_2_count:
            return False

    return True

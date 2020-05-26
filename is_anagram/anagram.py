

def is_anagram(str_1, str_2):
    str_1 = str_1.lower()
    str_2 = str_2.lower()
    for letter in str_1:
        if letter in str_2:
            letter_index = str_2.find(letter)
            if letter_index == 0:
                str_2 = str_2[letter_index+1:]
            elif letter_index < len(str_2):
                str_2 = str_2[:letter_index] + str_2[letter_index+1:]
            else:
                str_2 = str_2[:letter_index]
        else:
            return False
    if len(str_2) > 0:
        return False

    return True

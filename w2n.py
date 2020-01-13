numeral_words = {
    'один': 1,
    'два': 2,
    'три': 3
}


def make_numbers(str):
    words = str.split()
    return [numeral_words[w] if w in numeral_words else w for w in words]
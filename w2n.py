tokens_config = {
    'ноль': {'num': 0, 'level': 10},  # TODO: zero not allowed in complex numbers
    # TODO: need to add tokens 'double zero' and 'truple zero'
    'один': {'num': 1, 'level': 1},
    'одна': {'num': 1, 'level': 1},
    'два': {'num': 2, 'level': 1},
    'две': {'num': 2, 'level': 1},
    'три': {'num': 3, 'level': 1},
    'четыре': {'num': 4, 'level': 1},
    'пять': {'num': 5, 'level': 1},
    'шесть': {'num': 6, 'level': 1},
    'семь': {'num': 7, 'level': 1},
    'восемь': {'num': 8, 'level': 1},
    'девять': {'num': 9, 'level': 1},
    "десять": {'num': 10, 'level': 1},
    # TODO: there are not num tokens from 11 to 19
    "двадцать": {'num': 20, 'level': 2},
    "тридцать": {'num': 30, 'level': 2},
    "сорок": {'num': 40, 'level': 2},
    "пятьдесят": {'num': 50, 'level': 2},
    "шестьдесят": {'num': 60, 'level': 2},
    "семьдесят": {'num': 70, 'level': 2},
    "восемьдесят": {'num': 80, 'level': 2},
    "девяносто": {'num': 90, 'level': 2},
    "сто": {'num': 100, 'level': 3},
    "двести": {'num': 200, 'level': 3},
    "триста": {'num': 300, 'level': 3},
    "четыреста": {'num': 400, 'level': 3},
    "пятьсот": {'num': 500, 'level': 3},
    "шестьсот": {'num': 600, 'level': 3},
    "семьсот": {'num': 700, 'level': 3},
    "восемьсот": {'num': 800, 'level': 3},
    "девятьсот": {'num': 900, 'level': 3}
}


def make_num(text):
    words = text.split()
    numbers = []
    while words:
        if words[0] in tokens_config:
            num, words = make_num_greedy(words)
            numbers.append(num)
        else:
            words.pop(0)

    return ''.join([str(num) for num in numbers])


def make_num_versions(text):
    words = text.split()
    versions = make_num_versions_internal(words)
    return [''.join([str(num) for num in numbers]) for numbers in versions]


def make_num_versions_internal(words):
    if not words:
        return [[]]

    w = words[0]
    if w not in tokens_config:
        return[[make_num_versions_internal(words[1:])]]

    num_token = tokens_config[w]
    num_versions = set()
    versions = []

    for d in range(num_token['level'], 0, -1):
        num, rest = make_num_one_greedy(words, num_token['level'], d)
        if num not in num_versions:
            num_versions.add(num)
            versions.extend([[num] + v for v in make_num_versions_internal(rest)])
    return versions


def make_num_greedy(words):
    level = tokens_config[words[0]]['level']
    return make_num_one_greedy(words, level, level)


def make_num_one_greedy(words, level, depth):
    if not words or words[0] not in tokens_config or depth == 0:
        return 0, words
    num_token = tokens_config[words[0]]
    if num_token['level'] > level:
        return 0, words
    else:
        acc, rest = make_num_one_greedy(words[1:], level - 1, depth - 1)
        return acc + num_token['num'], rest

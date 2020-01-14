tokens_config = {
    'ноль': {'num': 0, 'type': 'self', 'level': 1},
    # TODO: need to add tokens 'double zero' and 'triple zero'
    'один': {'num': 1, 'type': 'final', 'level': 1},
    'одна': {'num': 1, 'type': 'final', 'level': 1},
    'два': {'num': 2, 'type': 'final', 'level': 1},
    'две': {'num': 2, 'type': 'final', 'level': 1},
    'три': {'num': 3, 'type': 'final', 'level': 1},
    'четыре': {'num': 4, 'type': 'final', 'level': 1},
    'пять': {'num': 5, 'type': 'final', 'level': 1},
    'шесть': {'num': 6, 'type': 'final', 'level': 1},
    'семь': {'num': 7, 'type': 'final', 'level': 1},
    'восемь': {'num': 8, 'type': 'final', 'level': 1},
    'девять': {'num': 9, 'type': 'final', 'level': 1},
    "десять": {'num': 10, 'type': 'final', 'level': 1},
    "одиннадцать": {'num': 11, 'type': 'final', 'level': 1},
    "двенадцать": {'num': 12, 'type': 'final', 'level': 1},
    "тринадцать": {'num': 13, 'type': 'final', 'level': 1},
    "четырнадцать": {'num': 14, 'type': 'final', 'level': 1},
    "пятнадцать": {'num': 15, 'type': 'final', 'level': 1},
    "шестнадцать": {'num': 16, 'type': 'final', 'level': 1},
    "семнадцать": {'num': 17, 'type': 'final', 'level': 1},
    "восемнадцать": {'num': 18, 'type': 'final', 'level': 1},
    "девятнадцать": {'num': 19, 'type': 'final', 'level': 1},
    "двадцать": {'num': 20, 'type': 'degree', 'level': 2},
    "тридцать": {'num': 30, 'type': 'degree', 'level': 2},
    "сорок": {'num': 40, 'type': 'degree', 'level': 2},
    "пятьдесят": {'num': 50, 'type': 'degree', 'level': 2},
    "шестьдесят": {'num': 60, 'type': 'degree', 'level': 2},
    "семьдесят": {'num': 70, 'type': 'degree', 'level': 2},
    "восемьдесят": {'num': 80, 'type': 'degree', 'level': 2},
    "девяносто": {'num': 90, 'type': 'degree', 'level': 2},
    "сто": {'num': 100, 'type': 'degree', 'level': 3},
    "двести": {'num': 200, 'type': 'degree', 'level': 3},
    "триста": {'num': 300, 'type': 'degree', 'level': 3},
    "четыреста": {'num': 400, 'type': 'degree', 'level': 3},
    "пятьсот": {'num': 500, 'type': 'degree', 'level': 3},
    "шестьсот": {'num': 600, 'type': 'degree', 'level': 3},
    "семьсот": {'num': 700, 'type': 'degree', 'level': 3},
    "восемьсот": {'num': 800, 'type': 'degree', 'level': 3},
    "девятьсот": {'num': 900, 'type': 'degree', 'level': 3}
}


def make_num(text):
    words = text.split()
    numbers = []
    while words:
        if words[0] in tokens_config:
            token = tokens_config[words[0]]
            num, words = make_num_greedy(words) if token['type'] != 'self' else (token['num'], words[1:])
            numbers.append(num)
        else:
            words.pop(0)

    return ''.join([str(num) for num in numbers])


# TODO: add limitation by length or prefix condition
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
    if num_token['type'] == 'self':
        num = num_token['num']
        return [[num] + v for v in make_num_versions_internal(words[1:])]

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
    if not words or words[0] not in tokens_config or depth == 0 or level == 0:
        return 0, words
    num_token = tokens_config[words[0]]
    if num_token['level'] > level or num_token['type'] == 'self':
        return 0, words

    if num_token['type'] == 'final':
        return num_token['num'], words[1:]

    acc, rest = make_num_one_greedy(words[1:], num_token['level'] - 1, depth - 1)
    return acc + num_token['num'], rest

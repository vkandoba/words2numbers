tokens_config = {
    'ноль': {'num': 0, 'level': 1},
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
}


def make_num(text):
    words = text.split()
    return [tokens_config[w]['num'] if w in tokens_config else w for w in words]
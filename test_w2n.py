from unittest import TestCase

from w2n import make_num, make_num_greedy, make_num_one_greedy


class TestMakeNumbers(TestCase):
    def test_make_with_empty(self):
        self.assertEqual('', make_num(''))

    def test_make_with_spaces(self):
        self.assertEqual('12', make_num('   один    два   '))

    def test_make_digits(self):
        self.assertEqual('9876543210', make_num('девять восемь семь шесть пять четыре три два один ноль'))

    def test_make_num(self):
        self.assertEqual('22264152', make_num('двести двадцать два шестьсот сорок один пятьдесят два'))

    def test_make_num_with_no_numerical_words(self):
        self.assertEqual('222641', make_num('номер двести двадцать два добавить шестьсот сорок один'))

    def test_make_one_greedy(self):
        self.assertEqual((5, []), make_num_one_greedy(['пять'], 1))
        self.assertEqual((45, []), make_num_one_greedy(['сорок', 'пять'], 2))
        self.assertEqual((205, []), make_num_one_greedy(['двести', 'пять'], 3))
        self.assertEqual((245, []), make_num_one_greedy(['двести', 'сорок', 'пять'], 3))

    def test_make_one_greedy_with_another_num_at_end(self):
        self.assertEqual((1, ['два']), make_num_greedy(['один', 'два']))
        self.assertEqual((200, ['триста']), make_num_greedy(['двести', 'триста']))
        self.assertEqual((200, ['ноль']), make_num_greedy(['двести', 'ноль']))
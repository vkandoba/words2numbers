from unittest import TestCase

from w2n import make_num, make_num_greedy, make_num_one_greedy


class TestMakeNumbers(TestCase):
    def test_make_with_empty(self):
        self.assertEqual([], make_num(''))

    def test_make_with_spaces(self):
        self.assertEqual([1, 2], make_num('   один    два   '))

    def test_make_digits(self):
        self.assertEqual([9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
                         make_num('девять восемь семь шесть пять четыре три два один ноль'))

    def test_make_greedy(self):
        self.assertEqual((245, []), make_num_one_greedy(['двести', 'сорок', 'пять'], 3))
        self.assertEqual((205, []), make_num_one_greedy(['двести', 'пять'], 3))

    def test_make_greedy_with_another_num_at_end(self):
        self.assertEqual((200, ['триста']), make_num_greedy(['двести', 'триста']))
        self.assertEqual((200, ['ноль']), make_num_greedy(['двести', 'ноль']))
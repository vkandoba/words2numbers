from unittest import TestCase

from w2n import make_num


class TestMakeNumbers(TestCase):
    def test_make_with_empty(self):
        self.assertEqual([], make_num(''))

    def test_make_with_spaces(self):
        self.assertEqual([1, 2], make_num('   один    два   '))

    def test_make_numbers(self):
        self.assertEqual([9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
                         make_num('девять восемь семь шесть пять четыре три два один ноль'))

from unittest import TestCase

from w2n import make_numbers


class TestMakeNumbers(TestCase):
    def test_make_numbers(self):
        self.assertEqual([1, 2, 3], make_numbers('один два три'))

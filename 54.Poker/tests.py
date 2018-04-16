import unittest as ut

from Poker import *


class PokerhandTest(ut.TestCase):
    pass

class ValueTest(ut.TestCase):
    def testCorrectValue(self):
        self.assertTrue(card_value("4")>card_value("2"))
        self.assertEquals(card_value('A'),14)
        self.assertEquals(card_value('T'),10)
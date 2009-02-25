import matcher_ness
from matcher_ness import MatcherNess
import unittest

class TestMatcher(unittest.TestCase):
    def setUp(self):
        self.m = MatcherNess('AAGCAGTGGTATCAACGCAGAGTACGCGGG')

    def test1(self):
        self.assertEquals('CAACT',(self.m.match('CAACTCCCGCGTACTCTGCGTTGATACCACTGCTTACTCT')))

    def test2(self):
        self.assertEquals('GTTGATACCGCTGCT',(self.m.match('GTTGATACCGCTGCTTACTCTGCGTTGATACCACTGCTTA')))

    def test3(self):
        self.assertEquals('GACGACTGATCGATC',(self.m.match('GACGACTGATCGATCTACTCTGCGTTGATACCACG')))

    def test4(self):
        self.assertEquals('GCTACTGATCATATCGTTAGCTAGCTAGCTACGT',(self.m.match('GCTACTGATCATATCGTTAGCTAGCTAGCTACGTCGTACT')))

    def test5(self):
        self.assertEquals('GAGCCAGGCT',(self.m.match('GCAGTGGTATCAACGCAGAGTACGCGGGGAGCCAGGCT')))

    def test6(self):
        self.assertEquals('AAGCAGTGGTATCAACGCAGA',(self.m.match('CAACGCAGAGTACGCGGGAAGCAGTGGTATCAACGCAGA')))


    def test7(self):
        self.assertEquals(None,(self.m.match('GCAGTGGTATCAACGCAGAGTAAGCCGTGGTATCAACGCA')))

if __name__ == "__main__":
    unittest.main()

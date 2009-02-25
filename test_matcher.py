import matcher
from matcher import Matcher
import unittest

class TestMatcher(unittest.TestCase):
	def setUp(self):
		self.m = Matcher('AAGCAGTGGTATCAACGCAGAGTACGCGGG')

	def test1(self):
		self.assertEquals('CAACT',(self.m.match('CAACTCCCGCGTACTCTGCGTTGATACCACTGCTTACTCT')))

	def test2(self):
		self.assertEquals('' ,(self.m.match('GTTGATACCGCTGCTTACTCTGCGTTGATACCACTGCTT')))

	def test3(self):
		self.assertEquals('GACGACTGATCGATC',(self.m.match('GACGACTGATCGATCTACTCTGCGTTGATACCACG')))

	def test4(self):
		self.assertEquals('GCTACTGATCATATCGTTAGCTAGCTAGCTACGT',(self.m.match('GCTACTGATCATATCGTTAGCTAGCTAGCTACGTCGTACT')))

	def test5(self):
		self.assertEquals('GAGCCAGGCT',(self.m.match('GCAGTGGTATCAACGCAGAGTACGCGGGGAGCCAGGCT')))

	def test6(self):
		self.assertEquals('AAGCAGTGGTATCAACGCAGA',(self.m.match('CAACGCAGAGTACGCGGGAAGCAGTGGTATCAACGCAGA')))

	def test7(self):
		self.assertEquals('TCT',(self.m.match('AGCTAGCTAGCTAGCTAATCAACGCAGAGTACGCGGGTCT')))

	def test8(self):
		self.assertEquals('AGCCGTGGTATCAACGCA',(self.m.match('GCAGTGGTATCAACGCAGAGTAAGCCGTGGTATCAACGCA')))

if __name__ == "__main__":
    unittest.main()

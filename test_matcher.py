import matcher
from matcher import Matcher
import unittest

class TestMatcher(unittest.TestCase):
    def setUp(self):
        self.m = Matcher("ADAPTOR")

    def testMatchesLeadingAdaptor(self):
        self.assert_(self.m.match("ADAPTORsequence"))

    def testDoesNotMatchMissingAdaptor(self):
        self.assert_(not self.m.match("sequence"))

    def testDoesNotMatchEmbeddedAdaptor(self):
        self.assert_(not self.m.match("sequenceADAPTORsequence"))

    def testMatchesAtLeastLastBaseOfAdaptor(self):
        self.assert_(self.m.match("Rsequence"))

    def testSplitOptionalRequired(self):
        self.assertEquals(("ADAP","TOR"), matcher.splitOptionalRequired("ADAPTOR",3))
        self.assertEquals(("ADA","PTOR"), matcher.splitOptionalRequired("ADAPTOR",-3))

    def testMatchesWithMinimumThresholdSet(self):
        m_min = Matcher("ADAPTOR",4)
        self.assert_(m_min.match("PTORsequence"))

    def testDoesNotMatchAdaptorWithValidPartialBelowThreshold(self):
        m_min = Matcher("ADAPTOR",4)
        self.assert_(not m_min.match("TORsequence"))

    def testDoesNotMatchAdaptorWithNonleadingBasesMissing(self):
        self.assert_(not self.m.match("AATRsequence"))

    def testMatchesPartialAdapter(self):
        self.assert_(self.m.match("DAPTORsequence"))

    def testMatchesAdaptorSuffix(self):
        self.assert_(self.m.match("sequenceADAPTOR"))

    def testMatchesPartialAdaptorSuffix(self):
        self.assert_(self.m.match("sequenceADAPT"))

    def testMatchResultPrefixMatchOnly(self):
        self.assertEquals("sequence",self.m.match("DAPTORsequence"))

    def testMatchResultSuffixMatchOnly(self):
        self.assertEquals("sequence",self.m.match("sequenceADAPTO"))

    def testMatchResultPrefixAndSuffix(self):
        self.assertEquals("sequence",self.m.match("DAPTORsequenceADAPTO"))

if __name__ == "__main__":
    unittest.main()

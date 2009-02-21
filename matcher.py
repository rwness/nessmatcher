import re

class Matcher:
    DEFAULT_MIN = 1

    def __init__(self, adapter, threshold=DEFAULT_MIN):
        (optional, required) = splitOptionalRequired(adapter, threshold)
        self.prefix_matcher = re.compile('^' + alternates(optional, lambda o,n: o[-n:]) + required + '(?P<seq>.*)' + '$')

        (required, optional) = splitOptionalRequired(adapter, -threshold)
        self.suffix_matcher = re.compile('^' + '(?P<seq>.*)' + required + alternates(optional, lambda o,n: o[0:n]) + '$')

    def match(self, sequence):
        pm = self.prefix_matcher.search(sequence)
        sm = self.suffix_matcher.search((pm and pm.group('seq')) or sequence)
        return (sm and sm.group('seq')) or (pm and pm.group('seq'))

# helper functions, not to be imported when using Matcher class
def splitOptionalRequired(adapter, index):
    return adapter[0:-index], adapter[-index:]

def alternates(optional, range_lambda):
    alternates = []
    for n in range(1, 1 + len(optional)):
        alternates.append(range_lambda(optional,n))
    return '(' + "|".join(alternates) + ')' + '?'

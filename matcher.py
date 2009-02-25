import re

class Matcher:
	EXT_THRESHOLD = 5
	INT_THRESHOLD = 15

	def __init__(self, adapter):
		self.pattern = re.compile('(?P<auxseq>.*?)' + make_pattern(adapter) + '(?P<targetseq>.*)')
		self.rc_pattern = re.compile ('(?P<targetseq>.*?)' + make_pattern(reverse_complement(adapter)) + '(?P<auxseq>.*?)')

	def match_pattern(self, sequence, pattern):
		match = pattern.search(sequence)
		if match and len(match.group('adapterseq')) > self.__class__.INT_THRESHOLD:
			return match.group('targetseq')
		elif match and len(match.group('auxseq')) == 0 and len(match.group('adapterseq')) > self.__class__.EXT_THRESHOLD:
			return match.group('targetseq')

	def match(self, sequence):
		return self.match_pattern(sequence, self.pattern) or self.match_pattern(sequence, self.rc_pattern)

# helper functions
def make_pattern(adapter):
	segments = [adapter[j:i + j]
		    for i in range(5,len(adapter) + 1)[::-1]
		    for j in range(0,len(adapter))
		    if i + j <= len(adapter)]
	return "(?P<adapterseq>" + "|".join(segments) + ")"

def reverse_complement(adapter):
	compliments = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
	return ''.join([compliments[base] for base in adapter][::-1])

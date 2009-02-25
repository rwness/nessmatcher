import re

class Matcher:
	EXT_THRESHOLD = 5
	INT_THRESHOLD = 15

	def __init__(self, adapter):
		self.rc = reverse_complement(adapter)
		self.pattern = re.compile('(?P<auxseq>.*?)' + make_search_pattern(adapter) + '(?P<targetseq>.*)')
		self.rc_pattern = re.compile ('(?P<targetseq>.*?)' + make_search_pattern(self.rc) + '(?P<auxseq>.*?)')

	def match_pattern(self, sequence, pattern):
		match = pattern.search(sequence)
		if match and len(match.group('adapterseq')) > self.__class__.INT_THRESHOLD:
			return match.group('targetseq')
		elif match and len(match.group('auxseq')) == 0 and len(match.group('adapterseq')) > self.__class__.EXT_THRESHOLD:
			return match.group('targetseq')

	def match(self, sequence):
		return self.match_pattern(sequence, self.pattern) or self.match_pattern(sequence, self.rc_pattern)

# helper functions
def make_search_pattern(adapter):
	windows = []
	window_size = len(adapter)
	i = 0
	j = (i + window_size-1)

	while window_size >= Matcher.EXT_THRESHOLD:
		i = 0
		j = j = (i + window_size)
		while j <= len(adapter):
			windows.append(adapter[i:j])
			i += 1
			j = (i + window_size)
		window_size -= 1
	return "(?P<adapterseq>" + "|".join(windows) + ")"

def reverse_complement(adapter):
	compliments = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
	return ''.join([compliments[base] for base in adapter][::-1])

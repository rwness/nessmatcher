import re

class MatcherNess:
	def __init__(self, adapter):
		self.adapter = adapter
		self.rc = reverse_complement(self.adapter)
		self.forward_seeker = re.compile('(?P<preseq>.*?)' + make_search_pattern(self.adapter) + '(?P<postseq>.*)')
		self.rc_seeker = re.compile ('(?P<preseq>.*?)' + make_search_pattern(self.rc) + '(?P<postseq>.*?)')

	def match_forward(self, sequence, ext_threshold = 5, int_threshold = 10):
		match_forward = self.forward_seeker.search(sequence)
		if match_forward and len(match_forward.group('adapterseq')) > int_threshold:
			return match_forward.group('postseq')
		elif match_forward and len(match_forward.group('preseq')) == 0 and len(match_forward.group('adapterseq')) > ext_threshold:
			return match_forward.group('postseq')
		else:
			return None

	def match_rc(self, sequence, ext_threshold = 5, int_threshold = 10):
		match_rc = self.rc_seeker.search(sequence)
		if match_rc and len(match_rc.group('adapterseq')) > int_threshold:
			return match_rc.group('preseq')
		elif match_rc and len(match_rc.group('postseq')) == 0 and len(match_rc.group('adapterseq')) > ext_threshold:
			return match_rc.group('preseq')
		else:
			return None

	def match(self, sequence, ext_threshold = 5, int_threshold = 10):
		self.match_forward(sequence, ext_threshold, int_threshold)
		return self.match_forward(sequence, ext_threshold, int_threshold) or self.match_rc(sequence, ext_threshold, int_threshold)

# helper functions

def make_search_pattern(adapter):
	alternates = []
	threshold = 5
	alternates.append(adapter)
	i = len(adapter) -1
	while i >= threshold:
		alternates.append(adapter[:i])
		alternates.append(adapter[-i:])
		i -= 1
	return "(?P<adapterseq>" + "|".join(alternates) + ")"

# this function takes the adapter and generates the reverse complement
def reverse_complement(adapter):
	reverse = adapter[::-1]
	rc = ''
	for ch in reverse:
		if ch == 'A':
			rc = rc + 'T'
		elif ch == 'C':
			rc = rc + 'G'
		elif ch == 'G':
			rc = rc + 'C'
		elif ch == 'T':
			rc = rc + 'A'
	return rc

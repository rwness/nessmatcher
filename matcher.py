import re

class Matcher:
	EXT_THRESHOLD = 5
	INT_THRESHOLD = 15

	def __init__(self, adapter):
		self.adapter = adapter
		self.rc = reverse_complement(self.adapter)
		self.forward_seeker = re.compile('(?P<preseq>.*?)' + make_search_pattern(self.adapter) + '(?P<postseq>.*)')
		self.rc_seeker = re.compile ('(?P<preseq>.*?)' + make_search_pattern(self.rc) + '(?P<postseq>.*?)')

	def match_forward(self, sequence):
		match_forward = self.forward_seeker.search(sequence)
		if match_forward and len(match_forward.group('adapterseq')) > self.__class__.INT_THRESHOLD:
			return match_forward.group('postseq')
		elif match_forward and len(match_forward.group('preseq')) == 0 and len(match_forward.group('adapterseq')) > self.__class__.EXT_THRESHOLD:
			return match_forward.group('postseq')
		else:
			return None

	def match_rc(self, sequence):
		match_rc = self.rc_seeker.search(sequence)
		if match_rc and len(match_rc.group('adapterseq')) > self.__class__.INT_THRESHOLD:
			return match_rc.group('preseq')
		elif match_rc and len(match_rc.group('postseq')) == 0 and len(match_rc.group('adapterseq')) > self.__class__.EXT_THRESHOLD:
			return match_rc.group('preseq')
		else:
			return None

	def match(self, sequence):
		return self.match_forward(sequence) or self.match_rc(sequence)

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

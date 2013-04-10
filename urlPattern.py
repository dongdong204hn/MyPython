# #!/usr/bin/env python

import re
def build_match_and_apply(pattern, search, replace):
	def make_pattern(word):
		return re.search(pattern, word)
	def apply_pattern(word):
		return re.sub(search, replace, word)
	return (make_pattern, apply_pattern)

patterns = (
	('[aoesh]$', '$', 'es'),
	('.+y$', 'y$', 'ies'))

rules = [build_match_and_apply(pattern, search, replace) for (pattern, search, replace) in patterns]

def plural(nonu):
	for (make_pattern, apply_pattern) in rules:
		if make_pattern(nonu):
			return apply_pattern(nonu)

	raise ValueError('not found the pattern')

print plural('watch')

words = 'HAWAII + IDAHO + IOWA + OHIO == STATES'

wordArray = re.findall('[A-Z]+', words.upper())
unique_words = set(''.join(wordArray))
print unique_words

digits = tuple(ord(c) for c in '0123456789')
print digits

joinwords = ''.join(wordArray)
print joinwords
print tuple(ord(c) for c in joinwords)
print eval('2344 + 324342 + 1')

#!/usr/bin/env python
print 'hello python'

import re
pattern = re.compile('\d+')

m =  re.search('(\d+)', '234 dfsaf')
if m:
	print m.group(0)
print dir(pattern)
if pattern.match('2344'):
	print pattern.groups()


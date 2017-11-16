import re

# Prepare data
data = []
with open('file.txt','r') as f:
	for line in f:
		data = data + map(lambda x:x.strip(),re.findall('\w+\s+',line))

# Functions
def find_anagram_1(data):
	WORDS = {}
	for word in data:
		if WORDS.has_key(''.join(sorted(word))):
			WORDS[''.join(sorted(word))].append(word)
		else:
			WORDS[''.join(sorted(word))] = []
			WORDS[''.join(sorted(word))].append(word)
	return WORDS

print find_anagram_1(data)

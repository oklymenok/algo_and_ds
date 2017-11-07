a="axfssdasdsaghjkflrtyfgdfsasdvbagahjkluoutyuiuyt"

def find_anagram(s):

	result = {}
	for i in range(len(s)):
		for j in range(i,len(s)):
			if (j-i)>1:
				tmp = s[i:j]
				if tmp[:] == tmp[::-1]:
					result.update({tmp:len(tmp)})
	return result
r = find_anagram(a)
mv = 0
for k,v in r.iteritems():
	if v>mv:
		mv=v
		mk=k
print mk

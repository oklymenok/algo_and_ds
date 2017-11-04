def d2r(num):
	rmap = [
			{"1000": "M"},
			{"500": "D"},
			{"100": "C"},
			{"50": "L"},
			{"10": "X"},
			{"5": "V"},
			{"1": "I"}
	]
	i = 0
	while num>0:
		if rmap[i].keys()[0].startswith("1") and num>=int(rmap[i].keys()[0]):
			m,r = divmod(num,int(rmap[i].keys()[0]))
			if m<4:
				yield m*rmap[i].values()[0]
			elif m == 4:
				yield rmap[i].values()[0]+rmap[i-1].values()[0]
			num = num - m*int(rmap[i].keys()[0])
			i = 0

		if rmap[i].keys()[0].startswith("5") and num>=int(rmap[i].keys()[0]):
			m = (num-int(rmap[i].keys()[0]))/int(rmap[i+1].keys()[0])
			if m<4:
				yield rmap[i].values()[0]+rmap[i+1].values()[0]*m
			elif m == 4:
				yield rmap[i+1].values()[0]+rmap[i-1].values()[0]
			num = num-int(rmap[i].keys()[0])-m*int(rmap[i+1].keys()[0])
			i = 0

		if num<int(rmap[i].keys()[0]):
			i = i + 1

print ''.join([x for x in d2r(1839)])

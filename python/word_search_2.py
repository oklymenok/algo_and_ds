data = [
		['o','a','a','n'],
		['e','t','a','e'],
		['i','h','k','r'],
		['i','f','l','v']
	]

words = ["oath","pea","eat","rain"]

def find_word(data,words):
	found_words = []
	for w in words:
		still_looking = True
		ln = 0
		while still_looking and ln<len(w)-1:
			
			r = lc(data,w[ln])
			if r:
				cx,cy = r[0],r[1]
			else:
				still_looking = False
		
			r = lc(data,w[ln+1])
			if r:
				nx,ny = r[0],r[1]
				if abs(cx-nx)<=1 and abs(cy-ny)<=1:
					ln = ln + 1
				else:
					still_looking = False
			else:
				still_looking = False

		if still_looking:
			found_words.append(w)
	return found_words

def lc(data,l):
	x=0
	y=0
	found = False
	while not found and x<len(data):
		if l in data[x]:
			found = True
			return x,data[x].index(l)
		else:
			x = x + 1
	return False

print find_word(data,words)

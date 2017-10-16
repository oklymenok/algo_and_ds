#/bin/env

data = [4,2,3,1,5,8,6,7]

for i in range(len(data)):
	mi = i
	for j in range(i,len(data)):
		if data[mi]>data[j]:
			mi = j
	tmp = data[i]
	data[i] = data[mi]
	data[mi] = tmp

#/bin/env python

data = [4,2,3,1,5,8,6,7]

def shift_array_right(data,num):
	for i in range(num):
		last = data[-1]
		for i in range(len(data)-1,0,-1):
			data[i]=data[i-1]
		data[0]=last
	return data

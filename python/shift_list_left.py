#!/bin/env python

data = [4,2,3,1,5,8,6,7]

def shift_array_left(data,num):
	if num == 0:
		return data
	if num > 0:
		for i in range(num):
			tmp = data.pop(0)
			data.append(tmp)
		return data

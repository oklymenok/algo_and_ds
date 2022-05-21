#!/bin/env

def reverse_list(data):
	if len(data) == 1:
		return [data[0]]
	else:
		return [data[-1]] + reverse_list(data[0:-1])

data = [1,2,3,4,5,6]
print(reverse_list(data))

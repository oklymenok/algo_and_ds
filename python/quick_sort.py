#!/usr/bin/python

data = [12,0,3,9,1,2,4,5,10,6,7,15]

def quick_sort(data,lm,rm):
	if rm>lm:
		splitpoint = partition(data,lm,rm)
		quick_sort(data,lm,splitpoint-1)
		quick_sort(data,splitpoint+1,rm)

def partition(data,lm,rm):
	p = lm
	lm = p + 1
	while rm>=lm:
		if data[lm]<data[p]:
			lm = lm + 1
		else:
			if data[rm]>data[p]:
				rm = rm - 1
			else:
				data[lm],data[rm] = data[rm],data[lm]
	data[p],data[rm] = data[rm],data[p]
	return rm

print "Before data: ",
print data
quick_sort(data,0,len(data)-1)
print "After data:  ",
print data

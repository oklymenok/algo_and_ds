#!/bin/evn python

data = [1,2,6,7,9,12,16,21,23,24,25,31,34,36,38,40]

def bin_search(data,num):
  if num>data[-1]:
    raise Exception
  right = len(data)-1
  left = 0
  while right > left:
    mid = (right+left)/2
    if num == data[mid]:
      return mid
    elif num > data[mid]:
      left = mid + 1
    elif num < data[mid]:
      right = mid - 1

a = bin_search(data,12)
print a

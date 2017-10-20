#!/bin/env python

a1 = [1,3,4,5,9,11,12,13,15]
a2 = [0,1,2,4,5,6,7,10,11,14,15,19,18]
#a2 = [2,3,5,8,10,11]
#a2 = []
#a2 = [-4,-2,0]

def find_common(first,second):
  counter = 0
  for i in first:
    if i in second:
      counter = counter + 1
  return counter

if len(a1) == 0 or len(a2) == 0:
  COUNTER = 0
elif a1[0] > a2[-1] or a2[0] > a1[-1]:
  COUNTER = 0
elif a1[-1] < a2[-1]:
  COUNTER = find_common(a1,a2)
elif a2[-1] < a1[-1]:
  COUNTER = find_common(a2,a1)
elif len(a1) > len(a2):
  COUNTER = find_common(a2,a1)
else:
  COUNTER = find_common(a1,a2)

print(COUNTER)

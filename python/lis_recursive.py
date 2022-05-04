#!/bin/env python

def count_seq_length(seq_head, data):
  if len(data) == 1:
    if seq_head < data[0]:
      return 1
    else:
      return 0

  max_subseq_length = 0

  for i, v in enumerate(data):
    if seq_head < v:
      tmp_seq_length = 1 + count_seq_length(v, data[i:])
      if tmp_seq_length > max_subseq_length:
        max_subseq_length = tmp_seq_length
  return max_subseq_length

def longest_subseq(data):
  length_max = 0
  for i,v  in enumerate(data):
    tmp_length = 1 + count_seq_length(v, data[i:])
    if tmp_length > length_max:
      length_max = tmp_length
  return length_max

def start_tests():

  print("Test data:       [1,2,4,3]")
  print("Expected result: 3")
  data = [1,2,4,3]
  r = longest_subseq(data)
  print("Test result: {}".format(r))
  print("*" * 30)

  print("Test data:       [10,9,2,5,3,7,101,18]")
  print("Expected result: 4")
  data = [10,9,2,5,3,7,101,18]
  r = longest_subseq(data)
  print("Test result: {}".format(r))
  print("*" * 30)

  print("Test data:       [10,22,9,33,21,50,41,60,80]")
  print("Expected result: 6")
  data = [10,22,9,33,21,50,41,60,80]
  r = longest_subseq(data)
  print("Test result: {}".format(r))
  print("*" * 30)

start_tests()

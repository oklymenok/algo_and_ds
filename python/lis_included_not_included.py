#!/bin/env python


nums = [0,3,1,6,2,2,7]

# the dict will have
# k = index of seq head
# v = length

seq_length = {}

# The full sequence = [head] + [data]
# head - head of the sequence
# data - subsequence
def count_seq(head, data):
  # recursion exit condition
  if len(data) == 1:
    if head < data[0]:
      return 1
    else:
      return 0
  else:
    # if the first item of the subsequence is greater
    # than the head, then subsequence is increasing
    # so the length = 1 + length(remaining_subsequence)
    if head < data[0]:
      # we assign a new head and shrink subseq by the
      # 1 element that we added to the length "1 + "
      return 1 + count_seq(data[0], data[1:len(data)])
    else:
      # if the the first item of the subsequence is
      # lesser, then subseq isn't increasing, so we
      # skip the element, do not add +1 to the subseq
      # lenght and shrink the data size by 1 element
      return count_seq(head, data[1:len(data)])

print("Sequence = {}".format(str(nums)))

# Main loop. Calculate increasing sequence size
# for every item in the list
for i,v in enumerate(nums):
  # If we haven't reached the last element we shrink the list
  # and pass it to the recursive function
  if i + 1 < len(nums):
    seq_length[i] = 1 + count_seq(v, nums[i+1:len(nums)])
  else:
    seq_length[i] = 1 + count_seq(v, nums[i:len(nums)])

print("Results = {}".format(str(seq_length)))
print("Max Length  = {}".format(str(max(seq_length.values()))))

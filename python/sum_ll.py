#!/bin/env python

class ListNode(object):
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def sum_of_ll(lp1, lp2):

  multiplier = 1
  cv = 0

  while True:
            
    # Checking if we reached end of the list
    if lp1.next is None and lp2.next is None:
      tmp_sum = lp1.val + lp2.val
      tmp_sum = tmp_sum * multiplier
      cv += tmp_sum
      break
            
    if lp1.next is None:
      tmp_sum = lp1.val + lp2.val
      tmp_sum = tmp_sum * multiplier
      cv += tmp_sum
      lp1.val = 0
      lp2 = lp2.next
    elif lp2.next is None:
      tmp_sum = lp1.val + lp2.val
      tmp_sum = tmp_sum * multiplier
      cv += tmp_sum
      lp2.val = 0
      lp1 = lp1.next
    else:
      tmp_sum = lp1.val + lp2.val
      tmp_sum = tmp_sum * multiplier
      cv += tmp_sum
      lp1 = lp1.next
      lp2 = lp2.next

    multiplier = multiplier * 10

  return cv

def populate_ll(val):

  # Handling a special case
  if len(val) == 1:
    return ListNone(val=val[0], next=None)

  for i,v in enumerate(val):
    # first item
    if i == 0:
      new_node = ListNode(val=0, next=None)
      result_list_head = ListNode(val=v, next=new_node)
      current_node = new_node
    # last item
    elif i + 1 == len(result_string):
      current_node.val = v
      current_node.next = None
    else:
      current_node.val = v
      new_node = ListNode(val=0, next=None)
      current_node.next = new_node
      current_node = new_node

  cn = result_list_head
  return cn

def run_tests():
  print("Starting tests ...")
  print("*"* 60)

  lp1_head = ListNode(val=2,next=None)
  lp1_head.next = ListNode(val=4, next=None)
  lp1_head.next.next = ListNode(val=3, next=None)
  lp2_head = ListNode(val=5, next=None)
  lp2_head.next = ListNode(val=6, next=None)
  lp2_head.next.next = ListNode(val=4, next=None)
  lp1 = lp1_head
  lp2 = lp2_head
  t1_result = sum_of_ll(lp1, lp2)
  print("L1 = [2,4,3], L2 = [5,6,4]")
  print("Expected = 807")
  print("Result = {}".format(str(t1_result)))

  
  lp1_head = ListNode(val=0, next=None)
  lp2_head = ListNode(val=0, next=None)
  lp1 = lp1_head
  lp2 = lp2_head
  t2_result = sum_of_ll(lp1, lp2)
  print("L1 = [0], L2 = [0]")
  print("Expected = 0")
  print("Result = {}".format(str(t2_result)))


  lp1_head = ListNode(val=9, next=None)
  lp1_head.next = ListNode(val=9, next=None)
  lp1_head.next.next = ListNode(val=9, next=None)
  lp1_head.next.next.next = ListNode(val=9, next=None)
  lp1_head.next.next.next.next = ListNode(val=9, next=None)
  lp1_head.next.next.next.next.next = ListNode(val=9, next=None)
  lp1_head.next.next.next.next.next.next = ListNode(val=9, next=None)

  lp2_head = ListNode(val=9, next=None)
  lp2_head.next = ListNode(val=9, next=None)
  lp2_head.next.next = ListNode(val=9, next=None)
  lp2_head.next.next.next = ListNode(val=9, next=None)
  lp1 = lp1_head
  lp2 = lp2_head
  t3_result = sum_of_ll(lp1, lp2)
  print("L1 = [9,9,9,9,9,9,9], L2 = [9,9,9,9]")
  print("Expected = 10009998")
  print("Result = {}".format(str(t3_result)))
  
run_tests()

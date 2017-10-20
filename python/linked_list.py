#!/bin/env python

class Node(object):
  def __init__(self,data=None):
    self.value = data
    self.next = None

class LinkedList(object):
  def __init__(self,head=None):
    self.head = head

  def print_list(self):
    # Print all nodes of linked list
    if self.head != None:
      node = self.head
      while node != None:
        if node.value != None:
          print node.value
          node = node.next
  
  def insert(self,new_node):
    # Insert node in the begging of the list
    if new_node != None:
      new_node.next = self.head
      self.head = new_node

  def append(self,new_node):
    # Add node to the end of the list
    if new_node != None:
      if self.head != None:
        node = self.head
        while node.next != None:
          node = node.next
        node.next = new_node
      else:
        self.head = new_node

  def insert_after(self,prev,new_node):
    if new_node != None:
      if self.head != None:
        node = self.head
      while node.value != prev:
        node = node.next
      new_node.next = node.next
      node.next = new_node

  def delete(self,val):
    # delete node that has value == val
    if self.head != None and self.head.value == val:
      self.head = self.head.next
    elif self.head != None:
      node = self.head
      while node.value != val:
        prev = node
        node = node.next
      prev.next = node.next
      node = None

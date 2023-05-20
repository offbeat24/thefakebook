#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
  def __init__(self, node_data):
    self.data = node_data
    self.next = None

class SinglyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def insert_node(self, node_data):
    node = SinglyLinkedListNode(node_data)

    if not self.head:
      self.head = node
    else:
      self.tail.next = node

    self.tail = node
def print_singly_linked_list(node, sep):
  while node:
    print(str(node.data))

    node = node.next

    if node:
      print(sep)


#
# Complete the 'deleteEven' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST listHead as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def deleteEven(listHead):
  head = listHead
  node = listHead
  pre_node = None
  while node is not None:
    if node.data % 2 == 0 :
      if node is not head :
        pre_node.next = node.next
      elif node is head :
        head = node.next
    else :
      pre_node = node
    node = node.next
  return head

if __name__ == '__main__':

  listHead_count = int(input().strip())

  listHead = SinglyLinkedList()

  for _ in range(listHead_count):
      listHead_item = int(input().strip())
      listHead.insert_node(listHead_item)

  result = deleteEven(listHead.head)

  print_singly_linked_list(result, '\n')

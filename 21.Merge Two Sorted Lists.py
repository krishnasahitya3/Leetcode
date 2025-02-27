#You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.


#Approach 1:
# Definition for singly-linked list.
from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    
class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]):
      dummy = node = ListNode()
      
      while list1 and list2:
        if list1.val <= list2.val:
          node.next = list1
          list1 = list1.next
          
        else:
          node.next = list2
          list2 = list2.next
          
        node = node.next
        
      node.next = list1 or list2
      return dummy.next
    
    
list1 = [1,2,4]
list2 = [1,3,4]
x = Solution()
x.mergeTwoLists(list1, list2)
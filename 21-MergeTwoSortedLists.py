# Done

"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val > list2.val:
            head = list2
            list2 = list2.next
        else:
            head = list1
            list1 = list1.next

        curr = head
        
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = list2
                curr = curr.next
                list2 = list2.next
                
            
        while list1:
            curr.next = list1
            curr = curr.next
            list1 = list1.next

        while list2:
            curr.next = list2
            curr = curr.next
            list2 = list2.next

        return head

def arrayToLinkedList(arr:List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    
    head = ListNode(arr[0])
    curr = head
    for i in range(1,len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next
    return head

def printLinkedListVal(node:Optional[ListNode]):
    if not node:
        print('[ ]')
    else:
        print('[',end=' ')
        while node:
            print(node.val, end=' ')
            node = node.next
        print(']')

soln = Solution()

printLinkedListVal(soln.mergeTwoLists(arrayToLinkedList([1,3,5,7]),arrayToLinkedList([2,4,6,8])))
printLinkedListVal(soln.mergeTwoLists(arrayToLinkedList([1,2,3,4,5,6,7]),arrayToLinkedList([8,9,10])))
printLinkedListVal(soln.mergeTwoLists(arrayToLinkedList([]),arrayToLinkedList([8,9,10])))
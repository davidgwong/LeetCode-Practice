"""
Done!

Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        i = head.next
        j = i.next

        head.next = None
        i.next = head
        if not j:
            return i
        else:
            return self.reverseListHelper(i,j)

    def reverseListHelper(self, i:Optional[ListNode], j:Optional[ListNode]) -> Optional[ListNode]:
        k = j.next
        j.next = i

        if not k:
            return j
        if not k.next:
            k.next = j
            return k
        else:
            return self.reverseListHelper(j,k)

def arrayToLinkedList(arr:List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    
    head = ListNode(arr[0])
    curr = head
    for i in arr[1:]:
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

head = arrayToLinkedList([0,1,2,3,4,5])
printLinkedListVal(head)
printLinkedListVal(soln.reverseList(head))

head = arrayToLinkedList([0])
printLinkedListVal(head)
printLinkedListVal(soln.reverseList(head))

head = arrayToLinkedList([0,1])
printLinkedListVal(head)
printLinkedListVal(soln.reverseList(head))

head = arrayToLinkedList([])
printLinkedListVal(head)
printLinkedListVal(soln.reverseList(head))

head = arrayToLinkedList([0,1,2])
printLinkedListVal(head)
printLinkedListVal(soln.reverseList(head))
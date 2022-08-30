# Done!

from typing import Optional, List
from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        p1 = head
        nodeStack = deque()

        while p1:
            nodeStack.append(p1)
            p1 = p1.next
        
        listLength = len(nodeStack)
        numToReorder = listLength // 2

        p1 = head
        p2 = head.next
        count = 0

        while count < numToReorder:
            p1.next = nodeStack.pop()
            p1.next.next = p2
            p1 = p2
            p2 = p2.next
            count += 1
        
        if listLength % 2 == 1:
            p1.next = None
        else:
            p2.next = None

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

head = arrayToLinkedList([1,2,3])
Solution().reorderList(head)
printLinkedListVal(head)

head = arrayToLinkedList([1,2,3,4])
Solution().reorderList(head)
printLinkedListVal(head)

head = arrayToLinkedList([1,2,3,4,5])
Solution().reorderList(head)
printLinkedListVal(head)
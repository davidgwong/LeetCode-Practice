# Done

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        currNode, endNode = head, head

        # When linked list contains just 1 ListNode
        if n == 1 and not head.next:
            return None

        for i in range(n):
            endNode = endNode.next
        
        # When n == length of linked list
        if not endNode:
            return head.next
        
        while endNode.next:
            currNode = currNode.next
            endNode = endNode.next
        
        currNode.next = currNode.next.next

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
        print('[]')
    else:
        print('[',end='')
        while node:
            print(node.val, end=',')
            node = node.next
        print(']')

head = [1,2,3,4,5]
n = 2
print("Answer: [1,2,3,5]. Output: ", end="")
printLinkedListVal(Solution().removeNthFromEnd(arrayToLinkedList(head),n))

head = [1]
n = 1
print("Answer: []. Output: ", end="")
printLinkedListVal(Solution().removeNthFromEnd(arrayToLinkedList(head),n))

head = [1,2]
n = 1
print("Answer: [1]. Output: ", end="")
printLinkedListVal(Solution().removeNthFromEnd(arrayToLinkedList(head),n))

head = [1,2]
n = 2
print("Answer: [2]. Output: ", end="")
printLinkedListVal(Solution().removeNthFromEnd(arrayToLinkedList(head),n))
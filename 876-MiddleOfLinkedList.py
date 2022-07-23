# Done

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        midNode, endNode = head, head
        mid, len = 0, 1

        while endNode.next:
            endNode = endNode.next
            len += 1
            while mid < len//2:
                midNode = midNode.next
                mid += 1
        return midNode

head = [1,2,3,4,5]
print("Answer: [3,4,5]. Output: ", end=""), printLinkedListVal(Solution().middleNode(arrayToLinkedList(head)))

head = [1,2,3,4,5,6]
print("Answer: [4,5,6]. Output: ", end=""), printLinkedListVal(Solution().middleNode(arrayToLinkedList(head)))

head = [1]
print("Answer: [1]. Output: ", end=""), printLinkedListVal(Solution().middleNode(arrayToLinkedList(head)))

head = [1,2]
print("Answer: [2]. Output: ", end=""), printLinkedListVal(Solution().middleNode(arrayToLinkedList(head)))
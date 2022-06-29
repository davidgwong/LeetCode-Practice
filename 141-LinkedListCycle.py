# Done #

"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""


from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next or not head.next.next:
            return False
        
        l, r = head.next, head.next.next

        while l or r:
            if l is r:
                return True
            if not l.next or not r.next or not r.next.next:
                return False
            l = l.next
            r = r.next.next
        
        return False

def arrToLinkedList(arr:List[int], pos:int) -> ListNode:
    head = ListNode(arr[0])
    curr = head

    for i in arr[1:]:
        curr.next = ListNode(arr[i])
        curr = curr.next
    if pos != -1:
        it = head
        for j in range(pos):
            it = it.next
        curr.next = it
    return head


soln = Solution()
print('Answer: False. Output: ', end=''), print(soln.hasCycle(arrToLinkedList([3,2,0,-4,1],-1)))
print('Answer: True. Output: ', end=''), print(soln.hasCycle(arrToLinkedList([3,2,0,-4,1],1)))
print('Answer: False. Output: ', end=''), print(soln.hasCycle(arrToLinkedList([0],-1)))
print('Answer: True. Output: ', end=''), print(soln.hasCycle(arrToLinkedList([0,1],0)))
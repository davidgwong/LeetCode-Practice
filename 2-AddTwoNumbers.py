from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# First attempt.
def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    x = listNodeToIntRev(l1)
    y = listNodeToIntRev(l2)
    return intToListNodeRev(x+y)

def listNodeToIntRev(x: Optional[ListNode]):
    node_iter = x
    x_val = 0
    pow_counter = 0
    if(x.next == None):
        return x.val
    while(node_iter.next != None):
        x_val = x_val + (10 ** pow_counter) * node_iter.val
        pow_counter += 1
        node_iter = node_iter.next
    return x_val + (10 ** pow_counter) * node_iter.val

def listNodeToInt(x: Optional[ListNode]):
    node_iter = x
    x_val = 0
    if(x.next == None):
        return x.val
    while(node_iter.next != None):
        x_val = x_val * 10 + node_iter.val
        node_iter = node_iter.next
    return (x_val * 10 + node_iter.val)

def intToListNodeRev(x):
    retNode = ListNode(x % 10, None)
    iterNode = retNode
    x = x // 10
    while(x >= 1):
        tempNode = ListNode(x % 10, None)
        iterNode.next = tempNode
        iterNode = tempNode
        x = x // 10
    return retNode

def intToListNode(x):
    retNode = ListNode(x % 10, None)
    x = x // 10
    while(x >= 1):
        retNode = ListNode(x % 10, retNode)
        x = x // 10
    return retNode

x1 = intToListNode(243)
y1 = intToListNode(564)
print("Should print 708: " + str(listNodeToInt(addTwoNumbers(x1,y1))))

x1 = intToListNode(9999999)
y1 = intToListNode(9999)
print("Should print 89990001: " + str(listNodeToInt(addTwoNumbers(x1,y1))))

x1 = intToListNode(249)
y1 = intToListNode(5649)
print("Should print 70401: " + str(listNodeToInt(addTwoNumbers(x1,y1))))

x1 = intToListNode(1000000000000000000000000000001)
y1 = intToListNode(564)
print("x1: " + str(listNodeToInt(x1)))
print("Should print 6640000000000000000000000000001: " + str(listNodeToInt(addTwoNumbers(x1,y1))))
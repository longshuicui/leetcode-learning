# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/3/12
@function:
"""
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(val=0)
    head = dummy
    borrow = 0
    while l1 is not None or l2 is not None:
        if not l1:
            val = l2.val
            l2 = l2.next
        elif not l2:
            val = l1.val
            l1 = l1.next
        elif l1 and l2:
            val = l1.val + l2.val
            l1 = l1.next
            l2 = l2.next
        num = (val + borrow) % 10
        node = ListNode(num)
        borrow = (val + borrow) // 10
        head.next = node
        head = head.next
    if borrow > 0:
        node = ListNode(borrow)
        head.next = node
    return dummy.next


l1=ListNode(2, ListNode(4, ListNode(9)))
l2=ListNode(5, ListNode(6, ListNode(4, ListNode(9))))

res=addTwoNumbers(l1, l2)

head=res
while head:
    print(head.val, end=" ")
    head=head.next

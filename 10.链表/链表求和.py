# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/20
@function: 链表求和
用单向链表表示十进制整数，求两个正整数的和，
如1234+34=1268
单向链表，不能使用其他数据结构
"""


class ListNode:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


def reverseLinked(head):
    prev=None
    while head:
        next=head.next
        head.next=prev
        prev=head
        head=next
    return prev


def addLinked(headA, headB):
    prev=None
    temp=0
    while headA or headB:
        if headA and headB:
            val=headA.val+headB.val
            headA = headA.next
            headB = headB.next
        elif headA:
            val=headA.val
            headA=headA.next
        elif headB:
            val=headB.val
            headB=headB.next
        curVal=(val+temp)%10 # 取余当前位
        temp=(val+temp)//10 # 取整进位
        node=ListNode(curVal)
        node.next=prev
        prev=node
        # current.next=node
        # current=node
    return prev


def printLinked(head):
    while head:
        print(head.val, end=" ")
        head=head.next


A=ListNode(1,ListNode(2,ListNode(3,ListNode(6))))
B=ListNode(6,ListNode(4))

reverseA=reverseLinked(A)
reverseB=reverseLinked(B)

head=addLinked(reverseA,reverseB)
printLinked(head)


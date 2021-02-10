# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/8
@function:
21. Merge Two Sorted Lists (Easy)
https://leetcode.com/problems/merge-two-sorted-lists/
题目描述
    给定两个增序的链表，试将其合并成一个增序的链表。
输入输出样例
    输入两个链表，输出一个链表，表示两个链表合并的结果。
    Input: 1->2->4, 1->3->4
    Output: 1->1->2->3->4->4
"""
class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def mergeTwoLists(l1,l2):
    dummy=ListNode(None)
    node=dummy
    while l1 and l2:
        if l1.value<=l2.value:
            node.next=l1
            l1=l1.next
        else:
            node.next=l2
            l2=l2.next
        node=node.next
    node.next=l1 if l1 else l2
    return dummy.next

l1=ListNode(1,ListNode(2,ListNode(4)))
l2=ListNode(1,ListNode(3,ListNode(4)))
res=mergeTwoLists(l1,l2)

while res:
    print(res.value)
    res=res.next

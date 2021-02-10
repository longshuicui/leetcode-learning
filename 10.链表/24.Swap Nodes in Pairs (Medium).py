# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/8
@function:
24. Swap Nodes in Pairs (Medium)
https://leetcode.com/problems/swap-nodes-in-pairs/
题目描述
    给定一个矩阵，交换每个相邻的一对节点。
输入输出样例
    输入一个链表，输出该链表交换后的结果。
    Input: 1->2->3->4
    Output: 2->1->4->3
题解
    利用指针进行交换操作
"""


class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def swapPairs(head):
    p = head
    if p and p.next:
        s = p.next
        p.next = s.next
        s.next = p
        head = s
        while p.next and p.next.next:
            s = p.next.next
            p.next.next = s.next
            s.next = p.next
            p.next = s
            p = s.next

    return head


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
head = swapPairs(head)

while head:
    print(head.value)
    head = head.next

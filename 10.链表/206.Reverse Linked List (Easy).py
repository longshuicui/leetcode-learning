# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/7
@function:
206. Reverse Linked List (Easy)
https://leetcode.com/problems/reverse-linked-list/
题目描述
    翻转一个链表。
输入输出样例
    输入一个链表，输出该链表翻转后的结果。
    Input: 1->2->3->4->5->nullptr
    Output: 5->4->3->2->1->nullptr
题解
    递归与非递归
"""


class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def reverseListRecursive(head, prev):
    if head is None:
        return prev
    next = head.next
    head.next = prev
    return reverseListRecursive(next, head)


def reverseListNonRecursive(head):
    prev=None
    while head:
        next=head.next
        head.next=prev
        prev=head
        head=next
    return prev


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
node=reverseListNonRecursive(head)

while node:
    print(node.value)
    node=node.next


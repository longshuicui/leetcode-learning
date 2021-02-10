# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/8
@function:
234. Palindrome Linked List (Easy)
https://leetcode.com/problems/palindrome-linked-list/
题目描述
    以 O(1) 的空间复杂度，判断链表是否回文。
输入输出样例
    输入是一个链表，输出是一个布尔值，表示链表是否回文。
    Input: 1->2->3->2->1
    Output: true
题解
    先用快慢指针找到链表中点，再把链表切成两半；然后把后半段翻转；最后比较两半是否相等。
"""
class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def isPalindrome(head):
    if head is None or head.next is None:
        return True
    slow, fast=head, head
    while fast.next and fast.next.next:
        slow=slow.next
        fast=fast.next.next
    slow.next=reverseList(slow.next)
    slow=slow.next
    while slow:
        if head.value != slow.value:
            return False
        head=head.next
        slow=slow.next
    return True


def reverseList(head):
    prev=None
    while head:
        next=head.next
        head.next=prev
        prev=head
        head=next
    return prev


head=ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
res=isPalindrome(head)
print(res)


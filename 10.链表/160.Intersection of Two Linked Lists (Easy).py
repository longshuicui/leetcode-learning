# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/8
@function:
160. Intersection of Two Linked Lists (Easy)
https://leetcode.com/problems/intersection-of-two-linked-lists/
题目描述
    给定两个链表，判断它们是否相交于一点，并求这个相交节点。
输入输出样例
    输入是两条链表，输出是一个节点。如无相交节点，则返回一个空节点。
题解
    假设链表A的头节点到相交点的距离为a，距离B的头节点到相交点的距离为b，相交点到
    链表终点的距离为c。我们使用两个指针，分别指向两个链表的头节点，并以相同的速度
    前进，若到达链表结尾，则移动到另一条链表的头节点继续前进。按照这种方法，两个
    指针会在a+b+c次前进后到达相交节点。

    利用环路去做
"""
class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def getIntersectionNode(headA, headB):
    if headA is None or headB is None:
        return None
    l1, l2=headA, headB
    while l1!=l2:
        l1=l1.next if l1 else headB
        l2=l2.next if l2 else headA
    return l1





a=[1,9,1,2,4]
b=[3,2,4]
head=ListNode(2,ListNode(4))
headA=ListNode(1,ListNode(9,ListNode(1,head)))
headB=ListNode(3,head)
node=getIntersectionNode(headA,headB)
print(node.value)

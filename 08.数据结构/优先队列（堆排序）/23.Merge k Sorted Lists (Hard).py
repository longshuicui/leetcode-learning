# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/5
@function:
23. Merge k Sorted Lists (Hard)
https://leetcode.com/problems/merge-k-sorted-lists/
题目描述
    给定 k 个增序的链表，试将它们合并成一条增序链表。
输入输出样例
    输入是一个一维数组，每个位置存储链表的头节点；输出是一条链表。
    Input:
    [1->4->5,
    1->3->4,
    2->6]
    Output: 1->1->2->3->4->4->5->6
题解
    方法一：暴力  空间复杂度 O(n) 时间复杂度 O(nlogn) 主要是排序的时间，其他时间都是O(n) n是节点总数
    1.遍历所有的链表将节点的值都放到一个数组里面
    2.对这个数组进行迭代和排序，获得一个合适的节点值
    3.创建一个新的排序链表
    方法二：一个一个比较 优先队列
    1.比较链表的头，获得最小的值
    2.选定的节点拓展最终的排序链表

"""
from queue import PriorityQueue

class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next


def mergeKListsBrute(lists):
    nodes=[] # 存放链表中所有的值
    head=point=ListNode(0) # 新的链表
    for l in lists:
        while l:
            nodes.append(l.val)
            l=l.next
    for x in sorted(nodes):
        point.next=ListNode(x)
        point=point.next
    return head.next


l1=ListNode(1,ListNode(4,ListNode(5)))
l2=ListNode(1,ListNode(3,ListNode(4)))
l3=ListNode(2,ListNode(6))

new=mergeKListsBrute([l1,l2,l3])

while new:
    print(new.val)
    new=new.next
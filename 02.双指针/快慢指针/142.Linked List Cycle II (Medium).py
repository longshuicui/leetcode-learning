# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/1/26
@function:
142. Linked List Cycle II (Medium)
https://leetcode.com/problems/linked-list-cycle-ii/
题目描述
    给定一个链表，如果有环路，找出环路的开始点。
输入输出样例
    输入是一个链表，输出是链表的一个节点。如果没有环路，返回一个空指针。
    3 -> 2 -> 0 -> 4 -> 2
    在这个样例中，值为 2 的节点即为环路的开始点。
题解
    快慢指针解法。链表找环路问题通用解法。
    给定两个指针， 分别为slow和fast，起始位置都在链表开头。每次fast前进两步，slow前进一步，如果fast可以走到尽头，那么说明没有
    环路；如果可以无限循环下去，那么说明一定有环路。就会存在一个时刻slow和fast相遇。当slow和fast第一次相遇时，将fast重新移动到
    链表开头，并让slow和fast每次前进一步。当第二次相遇时，既是环路的起点
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def detectCycle(head:ListNode):
    # 快慢双指针
    slow, fast = head, head

    # 判断是否为环路
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
        # 第一次相遇
        if fast==slow:
            break
    else:
        return None
    fast=head
    while fast!=slow:
        fast=fast.next
        slow=slow.next
    return fast



node1=ListNode(3)
node2=ListNode(2)
node3=ListNode(0)
node4=ListNode(-4)
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node2

node=detectCycle(node2)
print(node.val)
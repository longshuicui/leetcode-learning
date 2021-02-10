# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/9
@function:
101. Symmetric Tree (Easy)
https://leetcode.com/problems/symmetric-tree/
题目描述
    判断一个二叉树是否对称。
输入输出样例
    输入一个二叉树，输出一个布尔值，表示该树是否对称
题解
    判断一个树是否对称等价于判断左右子树是否对称，
    1.如果两个子树都为空指针，则他们相等或者对称
    2.如果两个子树只有一个为空指针，则他们不相等或者不对称
    3.如果两个子树根节点的值不相等，则他们不相等或者不对称
    4.递归处理
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def condition(left, right):
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    if left.val!=right.val:
        return False
    return condition(left.left, right.right) and condition(left.right, right.left)


def isSymmetric(root):
    if not root:
        return True
    return condition(root.left, root.right)


root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(2)
root.left.left=TreeNode(3)
root.left.right=TreeNode(4)
root.right.left=TreeNode(4)
root.right.right=TreeNode(3)
res=isSymmetric(root)
print(res)
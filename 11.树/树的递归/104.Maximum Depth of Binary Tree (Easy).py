# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/9
@function:
104. Maximum Depth of Binary Tree (Easy)
https://leetcode.com/problems/maximum-depth-of-binary-tree/
题目描述
    求一个二叉树的最大深度。
输入输出样例
    输入是一个二叉树，输出是一个整数，表示该树的最大深度。
题解
    使用递归
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

res = maxDepth(root)
print(res)

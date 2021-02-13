# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :  2021/02/13
@function:
669. Trim a Binary Search Tree (Medium)
https://leetcode.com/problems/trim-a-binary-search-tree/
题目描述
    给定一个二叉查找树和两个整数 L 和 R，且 L < R，试修剪此二叉查找树，使得修剪后所有
    节点的值都在 [L, R] 的范围内。
输入输出样例
    输入是一个二叉查找树和两个整数 L 和 R，输出一个被修剪好的二叉查找树。
题解
    利用二叉树的大小关系，进行修剪。左节点小于父节点，右节点大于父节点。给定取值范围，即可按照递归开始修剪

"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def trimBST(root, L, R):
    if not root:
        return root
    if root.val > R:
        return trimBST(root.left, L, R)
    if root.val < L:
        return trimBST(root.right, L, R)
    root.left = trimBST(root.left, L, R)
    root.right = trimBST(root.right, L, R)
    return root

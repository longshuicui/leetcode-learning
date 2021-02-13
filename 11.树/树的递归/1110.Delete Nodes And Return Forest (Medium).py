# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/9
@function:
1110. Delete Nodes And Return Forest (Medium)
https://leetcode.com/problems/delete-nodes-and-return-forest/
题目描述
    给定一个整数二叉树和一些整数，求删掉这些整数对应的节点后，剩余的子树。
输入输出样例
    输入是一个整数二叉树和一个一维整数数组，输出一个数组，每个位置存储一个子树（的根节点）。
题解
    考虑在什么时候断开指针。为便于寻找删除节点，建立一个哈希表方便查找
"""
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def helper(root, d, forest):
    if not root:
        return root

def delNodes(root, toDelete):
    pass


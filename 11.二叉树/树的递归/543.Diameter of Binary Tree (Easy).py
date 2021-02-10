# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/9
@function:
543. Diameter of Binary Tree (Easy)
https://leetcode.com/problems/diameter-of-binary-tree/
题目描述
    求一个二叉树的最长直径。直径的定义是   二叉树上任意两节点之间的 无向距离。
输入输出样例
    输入是一个二叉树，输出一个整数，表示最长直径。
题解
    利用递归处理。
    最长的路径长度是L+R+1
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1
        def depth(node):
            if not node: return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L+R+1)
            return max(L, R) + 1

        depth(root)
        return self.ans - 1


root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
a=Solution().diameterOfBinaryTree(root)
print(a)
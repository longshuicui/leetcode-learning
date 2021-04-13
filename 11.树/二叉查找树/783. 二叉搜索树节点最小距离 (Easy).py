# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/4/13
@function:
783. 二叉搜索树节点最小距离 (Easy)
https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/
给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
题解：
    BST二叉搜索树中序遍历就是一个增序的列表，相邻两个值的差是最小的

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """需要遍历每个节点，时间复杂度O(n), 不需要占用额外空间"""
    def minDiffInBST(self, root: TreeNode) -> int:
        self.ans=float("inf")
        self.pre=-1
        self.dfs(root)
        return self.ans

    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        curr=root.val
        if self.pre==-1:
            self.pre=curr
        else:
            self.ans=min(abs(self.pre-curr), self.ans)
            self.pre=curr
        self.dfs(root.right)


root=TreeNode(27)
root.right=TreeNode(34)
root.right.right=TreeNode(58)
root.right.right.left=TreeNode(50)
root.right.right.left.left=TreeNode(44)

solution=Solution()
res=solution.minDiffInBST(root)
print(res)

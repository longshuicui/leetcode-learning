# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/4/27
@function:
938. 二叉搜索树的范围和 (Easy)
https://leetcode-cn.com/problems/range-sum-of-bst/
给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和。
示例 1：
    输入：root = [10,5,15,3,7,null,18], low = 7, high = 15
    输出：32
示例 2：
    输入：root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
    输出：23
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rangeSumBST(root, low, high):
    ans=0
    def dfs(root, ans):
        if not root:
            return ans
        ans=dfs(root.left, ans)
        if low<=root.val<=high:
            ans+=root.val
        ans=dfs(root.right, ans)
        return ans
    ans=dfs(root, ans)
    return ans


root=TreeNode(10)
root.left=TreeNode(5)
root.right=TreeNode(15)
root.left.left=TreeNode(3)
root.left.right=TreeNode(7)
root.right.right=TreeNode(18)

res=rangeSumBST(root, 7, 15)
print(res)





# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :  2021/03/01
@function:
257. Binary Tree Paths (Easy)
https://leetcode.com/problems/binary-tree-paths/
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.
返回所有从根节点到叶子节点的路径

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binaryTreePaths(root):
    ans = []
    if not root:
        return ans
    path = []
    backtrack(root, ans, path)
    return ans


def backtrack(root, ans, path):
    if not (root.left or root.right):
        path.append(str(root.val))
        ans.append("->".join(path))
        path.pop()
        return
    path.append(str(root.val))
    if root.left:
        backtrack(root.left, ans, path)
    if root.right:
        backtrack(root.right, ans, path)
    path.pop()


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)

res = binaryTreePaths(root)
print(res)

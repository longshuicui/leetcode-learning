# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/5/17
@function:
993. 二叉树的堂兄弟节点 (Easy)
https://leetcode-cn.com/problems/cousins-in-binary-tree/
在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。
如果二叉树的两个节点深度相同，但 父节点不同 ，则它们是一对堂兄弟节点。
我们给出了具有唯一值的二叉树的根节点 root ，以及树中两个不同节点的值 x 和 y 。
只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true 。否则，返回 false。
示例 1：
    输入：root = [1,2,3,4], x = 4, y = 3
    输出：false
示例 2：
    输入：root = [1,2,3,null,4,null,5], x = 5, y = 4
    输出：true
示例 3：
    输入：root = [1,2,3,null,4], x = 2, y = 3
    输出：false

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isCousins(root, x, y):
    x_parent, x_depth, x_found=None, None, False
    y_parent, y_depth, y_found=None, None, False

    def dfs(node, depth, parent):
        if not node:
            return
        nonlocal x_parent, x_depth, x_found, y_parent, y_depth, y_found
        if node.val == x:
            x_parent, x_depth, x_found = parent, depth, True
        if node.val == y:
            y_parent, y_depth, y_found = parent, depth, True
        if x_found and y_found:
            return

        dfs(node.left, depth+1, node)
        if x_found and y_found:
            return
        dfs(node.right, depth+1, node)

    dfs(root, 0, None)
    return x_depth==y_depth and x_parent!=y_parent






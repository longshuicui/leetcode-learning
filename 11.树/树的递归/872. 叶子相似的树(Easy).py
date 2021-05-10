# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/5/10
@function:
872. 叶子相似的树 (Easy)
https://leetcode-cn.com/problems/leaf-similar-trees/
请考虑一棵二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列。
举个例子，如上图所示，给定一棵叶值序列为(6, 7, 4, 9, 8)的树。
如果有两棵二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。
如果给定的两个根结点分别为root1 和root2的树是叶相似的，则返回true；否则返回 false 。

示例 1：
    输入：root1 = [3,5,1,6,2,9,8,null,null,7,4],
         root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
    输出：true
示例 2：
    输入：root1 = [1], root2 = [1]
    输出：true
示例 3：
    输入：root1 = [1], root2 = [2]
    输出：false
示例 4：
    输入：root1 = [1,2], root2 = [2,2]
    输出：true

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(root, seq):
    if not root.left and not root.right:
        seq.append(root.val)
    else:
        if root.left:
            dfs(root.left,seq)
        if root.right:
            dfs(root.right, seq)


def leafSimilar(root1, root2):
    seq1, seq2=[],[]
    if root1:
        dfs(root1, seq1)
    if root2:
        dfs(root2, seq2)
    return seq1==seq2


root1=TreeNode(1, left=TreeNode(2), right=TreeNode(3))
root2=TreeNode(1, left=TreeNode(3), right=TreeNode(2))

res=leafSimilar(root1, root2)
print(res)
# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/9
@function:
110. Balanced Binary Tree (Easy)
https://leetcode.com/problems/balanced-binary-tree/
题目描述
    判断一个二叉树是否平衡。树平衡的定义是，对于树上的任意节点，其两侧节点的最大深度的差值不得大于 1。
输入输出样例
    输入是一个二叉树，输出一个布尔值，表示树是否平衡。
题解
    类似于求树的最大深度，不同之处在于：一是需要先处理子树的深度再进行比较；二是如果在处理子树发现已经
    不平衡了，就不要继续往下判断了，避免多余的判断
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def calculateDepth(root):
    if not root:
        return 0
    left, right=calculateDepth(root.left), calculateDepth(root.right) #计算左右节点的深度
    if left==-1 or right==-1 or abs(left-right)>1: # 判断节点高度差
        return -1
    return 1+max(left, right)

def isBalanced(root):
    return calculateDepth(root)!=-1

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(2)
root.left.left=TreeNode(3)
root.left.right=TreeNode(3)
root.left.left.left=TreeNode(4)
root.left.left.right=TreeNode(4)
res=isBalanced(root)
print(res)
# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/10
@function:
105. Construct Binary Tree from Preorder and Inorder Traversal (Medium)
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
题目描述
    给定一个二叉树的前序遍历和中序遍历结果，尝试复原这个树。已知树里不存在重复值的节点。
输入输出样例
    输入是两个一维数组，分别表示树的前序遍历和中序遍历结果；输出是一个二叉树。
"""
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preOrder, inOrder):
    if len(preOrder)==0:
        return None
    loc={}
    for i in range(len(preOrder)):
        loc[inOrder[i]]=i
    return buildTreeHelper(loc, preOrder, 0, len(preOrder)-1,0)



def buildTreeHelper(loc, preOrder, s0, e0, s1):
    if s0>e0:
        return None
    mid=preOrder[s1]
    index=loc[mid]
    leftLen=index-s0-1
    node=TreeNode(mid)
    node.left=buildTreeHelper(loc, preOrder, s0, index-1, s1+1)
    node.right=buildTreeHelper(loc,preOrder,index+1,e0,s1+2+leftLen)
    return node



preOrder=[4,9,20,15,7]
inOrder=[9,4,15,20,7]
node=buildTree(preOrder, inOrder)
print(node.__dict__)
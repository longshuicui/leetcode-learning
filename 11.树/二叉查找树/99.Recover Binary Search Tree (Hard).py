# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :  2021/02/13
@function:
99. Recover Binary Search Tree (Hard)
https://leetcode.com/problems/recover-binary-search-tree/
题目描述
    给定一个二叉查找树，已知有两个节点被不小心交换了，试复原此树。
输入输出样例
    输入是一个被误交换两个节点的二叉查找树，输出是改正后的二叉查找树。
题解
    使用中序遍历二叉查找树，同时设置一个prev指针，记录当前节点中序遍历时的前节点，
    如果当前节点小于prev的值，说明需要调整次序
"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recoverTree(root):
    mistake1=None
    mistake2=None
    prev=None
    mistake1, mistake2, prev=inOrder(root, mistake1, mistake2, prev)
    if mistake1 and mistake2:
        mistake1.val, mistake2.val=mistake2.val, mistake1.val
    return root


def inOrder(root, m1, m2, prev):
    if not root:
        return
    if root.left:
        m1, m2, prev=inOrder(root.left, m1, m2, prev)
    if prev and root.val<prev.val:
        if not m1:
            m1=prev
            m2=root
        else:
            m2=root
    prev=root
    if root.right:
        m1, m2, prev=inOrder(root.right,m1, m2, prev)
    return m1, m2, prev

root=TreeNode(3)
root.left=TreeNode(1)
root.right=TreeNode(4)
root.right.left=TreeNode(2)

root=recoverTree(root)

def printTree(root):
    if root is None:
        return
    printTree(root.left)
    print(root.val,end=" ")
    printTree(root.right)

printTree(root)
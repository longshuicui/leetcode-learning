# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/10
@function:
144. Binary Tree Preorder Traversal (Medium)
https://leetcode.com/problems/binary-tree-preorder-traversal/
题目描述
    不使用递归，实现二叉树的前序遍历.
输入输出样例
    输入一个二叉树，输出一个数组，为二叉树前序遍历的结果
题解
    递归本质上就是栈，用栈来实现前序遍历
"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preOrderTraversal(root):
    res=[]
    if not root:
        return res
    stack= [root]
    while len(stack)>0:
        node=stack[-1] # 栈顶
        stack.pop()
        res.append(node.val)
        if node.right: # 先右后左，保证左节点先遍历，因为后进先出，所以左节点要后入
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res



root=TreeNode(1)
root.right=TreeNode(2)
root.right.left=TreeNode(3)

res=preOrderTraversal(root)
print(res)




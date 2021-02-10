# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/10
@function:
前序遍历， 中序遍历， 后序遍历
前序遍历、中序遍历、后序遍历是三种深度优先搜索遍历二叉树的方式。
只是对节点访问顺序不同，其他都相同
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preOrder(root):
    """前序遍历：先遍历父节点，再遍历左节点，最后遍历右节点"""
    if not root:
        return
    print(root.val)
    preOrder(root.left)
    preOrder(root.right)


def inOrder(root):
    """中序遍历：先遍历左节点，再遍历父节点，最后遍历右节点"""
    if not root:
        return
    inOrder(root.left)
    print(root.val)
    inOrder(root.right)


def postOrder(root):
    """后续遍历：先遍历左节点，再遍历右节点，最后遍历父节点"""
    if not root:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.val)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

preOrder(root)  # 前序遍历

inOrder(root)  # 中序遍历

postOrder(root)  # 后续遍历

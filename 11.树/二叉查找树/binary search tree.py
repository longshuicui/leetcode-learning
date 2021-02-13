# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/10
@function:
二分查找树：
对于每个父节点，其左子树中所有节点的值小于等于父节点的值，其右子树中所有节点的值大于等于父节点的值。
对于一个二叉查找树，可以在O(nlogn)的时间内查找一个值是否存在。
从根节点开始，若当前节点的值大于查找值则往左走，若当前节点的值小于查找值则往右走。
二叉查找树是有序的，中序遍历就是排序号的数组
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def findMin(self):
        """左子节点小于等于父节点"""
        if self.root is None:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current

    def findMax(self):
        """右子节点大于等于父节点"""
        if self.root is None:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current

    def insert(self, val):
        node = TreeNode(val)
        if self.root is None:
            self.root = node
        else:
            current = self.root
            while True:
                if val < current.val:
                    if current.left is None:
                        current.left = node
                        return
                    current = current.left
                else:
                    if current.right is None:
                        current.right = node
                        return
                    current = current.right

    def search(self, val):
        current = self.root
        while current:
            if current.val == val:
                return current
            current = current.left if val < current.val else current.right
        return current


class BST:
    def insert(self, root, val):
        """二叉搜索树插入操作"""
        if root is None:
            root = TreeNode(val)
        elif val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
        return root

    def find(self, root, val):
        """二叉搜索树查询操作"""
        if root is None:
            return None
        if root.val == val:
            return root
        elif val < root.val:
            return self.find(root.left, val)
        else:
            return self.find(root.right, val)

    def findMin(self, root):
        """二叉搜索树返回最小值"""
        if root.left:
            return self.findMin(root.left)
        else:
            return root

    def findMax(self, root):
        """二叉搜素树返回最大值"""
        if root.right:
            return self.findMax(root.right)
        else:
            return root

    def remove(self, root, val):
        """二叉搜索树删除节点"""
        if root is None:
            return
        if val < root.val:
            root.left = self.remove(root.left, val)
        elif val > root.val:
            root.right = self.remove(root.right, val)
        else:
            if root.left and root.right:
                # 如果当前节点存在左右子树，需要用右子树的最小值代替当前节点的值，然后删除右子树的最小值，递归处理
                temp = self.findMin(root.right)
                root.val = temp.val
                root.right = self.remove(root.right, temp.val)  # 删除右子树的最小值
            elif root.left is None and root.right is None:
                # 如果当前节点左右子树都为空，直接删除该节点即可
                root = None
            elif root.left is None:
                root = root.right
            elif root.right is None:
                root = root.left
        return root

    def printTree(self, root):
        """中序遍历"""
        if root is None:
            return
        self.printTree(root.left)
        print(root.val, end=" ")
        self.printTree(root.right)



root=None
bst=BST()
root=bst.insert(root,10)
root=bst.insert(root,8)
root=bst.insert(root,6)
root=bst.insert(root,15)
node=bst.findMin(root)
print(node.__dict__)
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
        self.root=root

    def findMin(self):
        """左子节点小于等于父节点"""
        if self.root is None:
            return None
        current=self.root
        while current.left:
            current=current.left
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
        node=TreeNode(val)
        if self.root is None:
            self.root=node
        else:
            current=self.root
            while True:
                if val<current.val:
                    if current.left is None:
                        current.left=node
                        return
                    current=current.left
                else:
                    if current.right is None:
                        current.right=node
                        return
                    current=current.right

    def search(self, val):
        current=self.root
        while current:
            if current.val==val:
                return current
            current=current.left if val<current.val else current.right
        return current

def inOrder(root):
    """中序遍历"""
    if not root:
        return
    inOrder(root.left)
    print(root.val)
    inOrder(root.right)



bst=BinarySearchTree()
nums=[7, 5, 9, 8, 15, 16, 18, 17]
for num in nums:
    bst.insert(num)

print(bst.findMin().val)
print(bst.findMax().val)

inOrder(bst.root)



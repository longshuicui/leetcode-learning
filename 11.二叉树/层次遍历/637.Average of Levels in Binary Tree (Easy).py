# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/9
@function:
637. Average of Levels in Binary Tree (Easy)
https://leetcode.com/problems/average-of-levels-in-binary-tree/
题目描述
    给定一个二叉树，求每一层的节点值的平均数。
输入输出样例
    输入是一个二叉树，输出是一个一维数组，表示每层节点值的平均数。
题解
    广度优先搜索BFS，只需要一个队列分别存储当前层的节点和下一层的节点
"""

from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def averageOfLevelsDFS(root):
    """利用DFS，遍历尽当前分支，然后转移到另一分支。
    创建两个列表存放层节点的个数和计算加和结果。最后求平均值即可
    时间复杂度 O(n) n为树的节点总数
    空间复杂度 O(h) h为树的高度
    """
    def average(node, s, c, i):
        if not node: # 递归退出条件，当前指针为空，根据具体题目确定返回值是什么
            return
        s[i]=s.get(i,0)+node.val
        c[i]=c.get(i,0)+1
        average(node.left, s,c, i+1) # 继续往下递归
        average(node.right,s,c,i+1)

    count= {}
    res={}
    average(root,res, count,0)
    output=[res[i]/count[i] for i in range(len(res))]
    return output



def averageOfLevelsBFS(root):
    """广度优先搜索"""
    ans = []
    if not root:
        return ans
    queue=deque()
    queue.append(root)
    while len(queue)>0:
        count=len(queue)
        s=0
        for i in range(count):
            node=queue[0]
            queue.popleft()
            s+=node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        ans.append(s/count)
    return ans



root=TreeNode(3)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.right.left=TreeNode(15)
root.right.right=TreeNode(7)
out=averageOfLevelsBFS(root)
print(out)

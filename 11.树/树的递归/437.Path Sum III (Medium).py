# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/9
@function:
437. Path Sum III (Medium)
https://leetcode.com/problems/path-sum-iii/
题目描述
    给定一个整数二叉树，求有多少条路径节点值的和等于给定值。
输入输出样例
    输入一个二叉树和一个给定整数，输出一个整数，表示有多少条满足条件的路径。
题解
    如果选取该节点加入路径，则之后必须继续加入连续节点，或停止加入节点。
    如果不选取该节点加入路径，则对其左右节点进行重新考虑。
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pathSum(root, target):
    if not root:
        return 0
    return pathSumStartWithRoot(root, target)+pathSum(root.left, target)+pathSum(root.right, target)


def pathSumStartWithRoot(root, target):
    if not root:
        return 0
    if root.val==target:
        count=1
    else:
        count=0
    count+=pathSumStartWithRoot(root.left, target=target-root.val)
    count+=pathSumStartWithRoot(root.right, target=target-root.val)
    return count
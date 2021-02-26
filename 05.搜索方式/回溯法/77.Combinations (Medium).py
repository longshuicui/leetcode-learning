# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/1/30
@function:
77. Combinations (Medium)
https://leetcode.com/problems/combinations/

题目描述
    给定一个整数 n 和一个整数 k，求在 1 到 n 中选取 k 个数字的所有组合方法。
输入输出样例
    输入是两个正整数 n 和 k，输出是一个二维数组，表示所有组合方式。
    Input: n = 4, k = 2
    Output: [[2,4], [3,4], [2,3], [1,2], [1,3], [1,4]]
    这里二维数组的每个维度都可以以任意顺序输出。
题解
    类似于排列问题，我们也可以进行回溯。排列回溯的是 交换的位置 ，
    而组合回溯的是否把 当前的数字 加入结果中。
"""
from copy import deepcopy

def backtracking(ans, comb, count, pos, n, k):
    if count == k:
        ans.append(deepcopy(comb))
        return
    for i in range(pos, n + 1):
        comb[count] = i  # 修改当前节点状态
        count += 1
        backtracking(ans, comb, count, i + 1, n, k)  # 迭代子节点
        count -= 1  # 回改当前节点


def combine(n,k):
    ans=[]
    comb=[0 for _ in range(k)]
    count=0
    backtracking(ans, comb, count,1, n, k)
    return ans

ans=combine(4,2)
print(ans)



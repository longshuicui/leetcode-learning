# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/1/29
@function:
547. Number of Provinces (Medium)
https://leetcode.com/problems/number-of-provinces/
题目描述
    给定一个二维的 0-1 矩阵，如果第 (i, j) 位置是 1，则表示第 i 个人和第 j 个人是朋友。已知
    朋友关系是可以传递的，即如果 a 是 b 的朋友， b 是 c 的朋友，那么 a 和 c 也是朋友，换言之这
    三个人处于同一个朋友圈之内。求一共有多少个朋友圈。
输入输出样例
    输入是一个二维数组，输出是一个整数，表示朋友圈数量。因为朋友关系具有对称性，该二
    维数组为对称矩阵。同时，因为自己是自己的朋友，对角线上的值全部为 1。
    Input:
        [[1,1,0],
         [1,1,0],
         [0,0,1]]
    Output: 2
    在这个样例中， [1,2] 处于一个朋友圈， [3] 处于一个朋友圈。

题解
    该题与695题不同，每行代表一个节点，列代表是否存在相邻节点。
    695题有m*n个节点，该题有N个节点。
"""


def findCircleNum(isConnected):
    connected = {i:False for i in range(len(isConnected))}
    count=0
    def dfs(i):
        connected[i]=True
        for k in range(len(isConnected)):
            if isConnected[i][k]==1 and not connected[k]:
                dfs(k)
    for i in range(len(isConnected)):
        if not connected[i]:
            dfs(i)
            count+=1
    return count


isConnected = [[1,1,0],[1,1,0],[0,0,1]]
count=findCircleNum(isConnected)
print(count)
# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/1
@function:
542. 01 Matrix (Medium)
https://leetcode.com/problems/01-matrix/
题目描述
    给定一个由 0 和 1 组成的二维矩阵，求每个位置到最近的 0 的距离。
输入输出样例
    输入是一个二维 0-1 数组，输出是一个同样大小的非负整数数组，表示每个位置到最近的 0
    的距离。
    Input:
        [[0,0,0],
         [0,1,0],
         [1,1,1]]
    Output:
        [[0,0,0],
         [0,1,0],
         [1,2,1]]

题解
    如果使用BFS，最坏的时间复杂度是O(m*m*n*n)
    从左上到右下做一次动态搜索，从右下到左上做一次动态搜索。即可以完成四个方向的搜索
"""


def updateMatrix(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return []
    m, n = len(matrix), len(matrix[0])
    dp = [[1e10 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:  # 如果矩阵某位置为0，那么对应的动态矩阵位置也为0
                dp[i][j] = 0
            else:
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if matrix[i][j] != 0:
                if j < n - 1:
                    dp[i][j] = min(dp[i][j], dp[i][j + 1] + 1)
                if i < m - 1:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)
    return dp


matrix = [[0, 0, 0],
          [0, 1, 0],
          [1, 1, 1]]
dp = updateMatrix(matrix)
print(dp)

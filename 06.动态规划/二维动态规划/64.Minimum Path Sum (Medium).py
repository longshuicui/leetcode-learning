# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/1
@function:
64. Minimum Path Sum (Medium)
https://leetcode.com/problems/minimum-path-sum/
题目描述
    给定一个 m × n 大小的非负整数矩阵，求从左上角开始到右下角结束的、经过的数字的和最
    小的路径。每次只能向右或者向下移动。
输入输出样例
    输入是一个二维数组，输出是最优路径的数字和。
    Input:
    [[1,3,1],
    [1,5,1],
    [4,2,1]]
    Output: 7
    在这个样例中，最短路径为 1->3->1->1->1。
题解
    定义一个二维的dp数组，dp[i][j]表示从左上角开始到（i，j）位置的最优路径的数字和。
    每次只能向下或者向右移动，所以状态转移方程为
    dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]
"""


def minPathSum(grid):
    dp=[[0]*len(grid[0])]*len(grid)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i==0 and j==0:
                dp[i][j]=grid[i][j]
            elif i==0:
                dp[i][j]=grid[i][j]+dp[i][j-1]
            elif j==0:
                dp[i][j]=grid[i][j]+dp[i-1][j]
            else:
                dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]
    return dp[-1][-1]



grid=[[1,2,3],
      [4,5,6]]
res=minPathSum(grid)
print(res)
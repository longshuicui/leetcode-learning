# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/2
@function:
221. Maximal Square (Medium)
https://leetcode.com/problems/maximal-square/
题目描述
    给定一个二维的 0-1 矩阵，求全由 1 构成的  最大正方形  面积。
输入输出样例
    输入是一个二维 0-1 数组，输出是最大正方形面积。
    Input:
    [["1","0","1","0","0"],
     ["1","0","1","1","1"],
     ["1","1","1","1","1"],
     ["1","0","0","1","0"]]
    Output: 4
题解
    对于矩阵内搜索正方形和长方形的题型，常见的做法就是定义一个二维dp数组。
    dp[i][j]表示满足条件的、以(i,j)为右下角的正方形或者长方形的属性。
    对于本题，表示以(i,j)为右下角的全由1构成的最大正方形面积。
    如果当前位置为0，那么dp[i][j]即为0；如果当前位置为1，假设dp[i][j]=k*k，
    其充分条件为dp[i-1][j-1]、dp[i][j-1]、dp[i-1][j]的值都不小于(k-1)*(k-1)
    否则(i,j)位置不可能构成一个边长为k的正方形。


"""


def maximalSquare(matrix):
    if len(matrix)==0 or len(matrix[0])==0:
        return 0
    m,n=len(matrix), len(matrix[0])
    maxSide=0
    dp=[[0 for _ in range(n+1)] for _ in range(m+1)] # 最大问题，初始化为0， 最小化问题，初始化为极大值
    for i in range(1,m+1):
        for j in range(1,n+1):
            if matrix[i-1][j-1]=="1":
                dp[i][j]=min(dp[i-1][j-1],min(dp[i][j-1],dp[i-1][j]))+1
            maxSide=max(maxSide,dp[i][j])
    return maxSide*maxSide





matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]
s=maximalSquare(matrix)
print(s)












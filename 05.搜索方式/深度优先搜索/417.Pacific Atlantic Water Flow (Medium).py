# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/1/29
@function:
417. Pacific Atlantic Water Flow (Medium)
https://leetcode.com/problems/pacific-atlantic-water-flow/
题目描述
    给定一个二维的非负整数矩阵，每个位置的值表示海拔高度。假设左边和上边是太平洋，右
    边和下边是大西洋，
    求从哪些位置向下流水，可以流到太平洋和大西洋。
    水只能从海拔高的位置流到海拔低或相同的位置。
输入输出样例
    输入是一个二维的非负整数数组，表示海拔高度。输出是一个二维的数组，其中第二个维度
    大小固定为 2，表示满足条件的位置坐标。
    Input:
        太平洋 ~ ~ ~ ~ ~
        ~ 1 2 2 3 (5) *
        ~ 3 2 3 (4) (4) *
        ~ 2 4 (5) 3 1 *
        ~ (6) (7) 1 4 5 *
        ~ (5) 1 1 2 4 *
        * * * * * 大西洋
    Output: [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
    在这个样例中，有括号的区域为满足条件的位置。

题解
    如果向下流能到达两个大洋的位置，搜索复杂度会非常高。如果大洋向上流，只需要对四条边进行搜索即可。
"""

def pacificAtlantic(matrix):
    if len(matrix)==0 or len(matrix[0])==0:
        return []
    canReachP=[[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    canReachA=[[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    ans=[]

    def dfs(r,c,canReach):
        if canReach[r][c]:
            return
        canReach[r][c]=True
        for nr, nc in ((r+1,c),(r-1,c),(r,c-1),(r,c+1)):
            if 0<=nr<len(matrix) and 0<=nc<len(matrix[0]) and matrix[r][c]<=matrix[nr][nc]:
                dfs(nr,nc,canReach)

    for i in range(len(matrix)):
        dfs(i, 0, canReachP) # 每行左侧开始 太平洋
        dfs(i, len(matrix[0])-1, canReachA) # 每行右侧开始 大西洋
    for j in range(len(matrix[0])):
        dfs(0, j, canReachP) # 每列上侧开始 太平洋
        dfs(len(matrix)-1, j, canReachA) # 每列下侧开始 大西洋

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if canReachP[i][j] and canReachA[i][j]:
                ans.append([i,j])
    return ans


matrix=[[1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4]]
ans=pacificAtlantic(matrix)
print(ans)
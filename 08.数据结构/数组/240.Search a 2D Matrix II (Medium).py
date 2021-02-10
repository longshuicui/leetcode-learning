# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/3
@function:
240. Search a 2D Matrix II (medium)
https://leetcode.com/problems/search-a-2d-matrix-ii/
题目描述
    给定一个二维矩阵，已知每行和每列都是增序的，尝试设计一个快速搜索一个数字是否在矩阵中存在的算法。
输入输出样例
    输入是一个二维整数矩阵，和一个待搜索整数。输出是一个布尔值，表示这个整数是否存在于矩阵中。
    Input: matrix =
        [[1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]], target = 5
    Output: true
题解
    从右上角开始搜索，如果值小于目标值则往下搜，如果值大于目标值则往左搜
"""


def searchMatrix(matrix, target):
    if len(matrix)==0:
        return False
    m,n=len(matrix), len(matrix[0])
    i,j=0,n-1 # 右上坐标
    while i<m and j>=0:
        if matrix[i][j]==target:
            return True
        elif matrix[i][j]>target:
            j-=1
        else:
            i+=1
    return False


matrix=[[1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]]
target=16
res=searchMatrix(matrix, target)
print(res)
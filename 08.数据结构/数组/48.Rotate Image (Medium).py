# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/3
@function:
48. Rotate Image (Medium)
https://leetcode.com/problems/rotate-image/
题目描述
    给定一个 n × n 的矩阵，求它顺时针旋转 90 度的结果，且必须在原矩阵上修改（in-place）。O(1)空间复杂度
输入输出样例
    输入和输出都是一个二维整数矩阵。
    Input:
        [[1,2,3],
         [4,5,6],
         [7,8,9]]
    Output:
        [[7,4,1],
         [8,5,2],
         [9,6,3]]

题解
    每次只考虑四个间隔90度的位置，可以进行O(1)的额外空间旋转
"""
def rotate(matrix):
    n=len(matrix)-1
    for i in range(n//2+1):
        for j in range(i,n-i):
            matrix[j][n-i],matrix[i][j],matrix[n-j][i],matrix[n-i][n-j]=\
                matrix[i][j],matrix[n-j][i],matrix[n-i][n-j],matrix[j][n-i]

    return matrix

matrix=[[1,2,3],[4,5,6],[7,8,9]]
matrix=rotate(matrix)
print(matrix)
# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/4/23
@function:
304. 二维区域和检索 - 矩阵不可变 (Medium)
https://leetcode-cn.com/problems/range-sum-query-2d-immutable/
给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2) 。
matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
"""

class NumMatrix:
    """二维数组的前缀和， 和一维数组一样, 初始化时间复杂度为O(m*n), 查询时间复杂度为O(1)"""
    def __init__(self, matrix):
        self.sum=[[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)]
        for i in range(1,len(matrix)+1):
            for j in range(1, len(matrix[0])+1):
                self.sum[i][j]=self.sum[i-1][j]+self.sum[i][j-1]-self.sum[i-1][j-1]+matrix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res=self.sum[row2+1][col2+1]-(self.sum[row2+1][col1]+self.sum[row1][col2+1])+self.sum[row1][col1]
        return res

matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
obj=NumMatrix(matrix)
print(obj.sumRegion(2, 1, 4, 3))
print(obj.sumRegion(1, 1, 2, 2))
print(obj.sumRegion(1, 2, 2, 4))
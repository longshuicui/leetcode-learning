# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/3/23
@function:
74. 搜索二维矩阵 (Medium)
https://leetcode-cn.com/problems/search-a-2d-matrix/
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
"""


def searchMatrix(matrix, target):
    m,n=len(matrix), len(matrix[0])
    left, right=0, m*n-1
    while left<=right:
        mid=left+(right-left)//2
        row=mid//n
        col=mid%n
        if target==matrix[row][col]:
            return True
        elif target>matrix[row][col]:
            left=mid+1
        else:
            right=mid-1
    return False


matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target=20
res=searchMatrix(matrix, target)
print(res)

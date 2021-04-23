# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/4/22
@function:
363. 矩形区域不超过 K 的最大数值和 (Hard)
https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k/
给你一个 m x n 的矩阵 matrix 和一个整数 k ，找出并返回矩阵内部矩形区域的不超过 k 的最大数值和。
题目数据保证总会存在一个数值和不超过 k 的矩形区域。
示例：
    输入：matrix = [[1,0,1],[0,-2,3]], k = 2
    输出：2
    输入：matrix = [[2,2,-1]], k = 3
    输出：3
"""


def maxSumSubmatrixBrute(matrix, k):
    m, n=len(matrix), len(matrix[0])
    # 生成前缀和 O(m*n)
    sum_=[[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            sum_[i][j]=sum_[i-1][j]+sum_[i][j-1]-sum_[i-1][j-1]+matrix[i-1][j-1]

    # 转换成了一维问题
    maxVal = -float("inf")
    if m==1:
        for j in range(1,n+1):
            for q in range(j+1, n+1):
                sumRegion=sum_[1][q]-sum_[1][j-1]
                if maxVal < sumRegion <= k:
                    maxVal = sumRegion
        return maxVal
    if n==1:
        for i in range(1,m+1):
            for p in range(i+1, m+1):
                sumRegion=sum_[p][1]-sum_[i-1][1]
                if maxVal < sumRegion <= k:
                    maxVal = sumRegion
        return maxVal

    # 根据304题，可以得出每个区域的面积，和k值比较就ok了
    # 这里的时间复杂度是O(m*m*n*n)
    # row1=i, col1=j, row2=p, col2=q
    for i in range(1, m+1):
        for j in range(1, n+1):
            for p in range(i+1, m+1):
                for q in range(j+1, n+1):
                    sumRegion=sum_[p][q]-(sum_[p][j-1]+sum_[i-1][q])+sum_[i-1][j-1]
                    if maxVal<sumRegion<=k:
                        maxVal=sumRegion
    return maxVal

matrix = [[2, 2, -1]]
k = 3
res=maxSumSubmatrixBrute(matrix, k)
print(res)
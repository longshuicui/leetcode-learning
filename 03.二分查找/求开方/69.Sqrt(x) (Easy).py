# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/1/26
@function:

69. Sqrt(x) (Easy)
https://leetcode.com/problems/sqrtx/
题目描述
    给定一个非负整数，求它的开方，向下  取整 。
输入输出样例
    输入一个整数，输出一个整数。
    Input: 8
    Output: 2
    8 的开方结果是 2:82842:::，向下取整即是 2。
题解
    二分法，类似双指针，指针每次走一半
"""


def mySqrt(x):
    if x==0:
        return 0
    l, r=1, x # 因为向下取整，所以left指针从1开始即可
    while l<=r:
        mid=l+(r-l)//2
        sqrt=x//mid
        if mid==sqrt:
            return mid
        elif mid>sqrt:
            r=mid-1
        else:
            l=mid+1
    return r


def newSqrt(x):
    temp=x
    while temp*temp>x:
        temp=(temp+x/temp)//2
    return int(temp)


num=newSqrt(8)
print(num)
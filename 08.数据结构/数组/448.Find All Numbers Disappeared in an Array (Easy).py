# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/3
@function:
448. Find All Numbers Disappeared in an Array (Easy)
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
题目描述
    给定一个长度为 n 的数组，其中包含范围为 1 到 n 的整数，有些整数重复了多次，有些整数
    没有出现，求 1 到 n 中没有出现过的整数。
输入输出样例
    输入是一个一维整数数组，输出也是一个一维整数数组，表示输入数组内没出现过的数字。
    Input: [4,3,2,7,8,2,3,1]
    Output: [5,6]

题解
    创建一个数组，对原数组进行标记，把重复出现得数字在原数组出现得位置设置为负数，
    最后仍为正数的位置即为没有出现过的数
"""

def findDisappearedNumbers(nums):
    n=len(nums)
    pos=[1]*(n+1)
    for i in nums:
        pos[i]=-1
    ans=[]
    for i in range(n+1):
        if i!=0 and pos[i]>0:
            ans.append(i)
    return ans

nums=[4,3,2,7,8,2,3,1]
ans=findDisappearedNumbers(nums)
print(ans)


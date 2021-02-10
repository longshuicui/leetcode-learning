# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/1
@function:
413. Arithmetic Slices (Medium)
https://leetcode.com/problems/arithmetic-slices/
题目描述
    给定一个数组，求这个数组中连续且等差的子数组一共有多少个。返回等差数列的个数
输入输出样例
    输入是一个一维数组，输出是满足等差条件的连续字数组个数。
    Input: nums = [1,2,3,4]
    Output: 3
    在这个样例中，等差数列有 [1,2,3]、 [2,3,4] 和 [1,2,3,4]。
题解
    要求是等差数列，所以满足 nums[i]-nums[i-1]=nums[i-1]-nums[i-2]
    返回等差数列的个数，数列中元素的个数不能小于三个
    该题最后需要对dp数组求和
"""


def numberOfArithmeticSlices(nums):
    if len(nums)<3:
        return 0
    dp=[0,0]
    for i in range(2,len(nums)):
        if nums[i]-nums[i-1]==nums[i-1]-nums[i-2]:
            dp.append(dp[i-1]+1)
        else:
            dp.append(0)
    return sum(dp)


nums=[1,2,3,5,6,7,8]
cnt=numberOfArithmeticSlices(nums)
print(cnt)
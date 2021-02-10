# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/3
@function:
53. Maximum Subarray (Easy)
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
给定一个整数数组，找出一个连续的子数组（至少包含一个数字），该数组的和最大，返回这个数组的和
Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6

题解
    dp[i]位置的值为dp[i-1]位置的数加上当前nums[i]数的和nums[i]中的最大值。
"""


def maxSubArray(nums):
    dp = [0 for _ in range(len(nums))]
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(dp[i - 1] + nums[i], nums[i])
    return max(dp)


nums=[-2,-8]
s=maxSubArray(nums)
print(s)
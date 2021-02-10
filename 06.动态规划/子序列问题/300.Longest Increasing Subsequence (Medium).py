# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/2
@function:
300. Longest Increasing Subsequence (Medium)
https://leetcode.com/problems/longest-increasing-subsequence/
题目描述
    给定一个未排序的整数数组，求  最长  的  递增  子序列的长度。
     注意 按照 LeetCode 的习惯，子序列（subsequence）不必连续，子数组（subarray）或子字符串
    （substring）必须连续。
输入输出样例
    输入是一个一维数组，输出是一个正整数，表示最长递增子序列的长度。
    Input: [10,9,2,5,3,7,101,18]
    Output: 4
    在这个样例中，最长递增子序列之一是 [2,3,7,18]。
题解
    求最长上升子序列的长度， 动态规划
    第一种方法，定义一个dp数组，其中dp[i]表示以i结尾的子序列的性质。在处理好每个位置之后，统计一遍各个位置的结果
    可以得到题目要求的结果。对于每一个位置i，如果其之前的某个位置j所对的数字小于所对应的数字，则我们可以获得一个以
    i结尾的长度为dp[j]+1的子序列。需要遍历两遍， 时间复杂度为O(n**n)
"""
def lengthOfLIS(nums):
    max_length=0
    if len(nums)<=1:
        return len(nums)
    dp=[1 for _ in range(len(nums))]
    for i in range(len(nums)):
        for j in range(0,i):
            if nums[i]>nums[j]:
                dp[i]=max(dp[i],dp[j]+1)
        max_length=max(max_length,dp[i])
    return max_length



nums=[10,9,2,5,3,7,101,18]
res=lengthOfLIS(nums)
print(res)


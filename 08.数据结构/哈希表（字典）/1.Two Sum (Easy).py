# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/7
@function:
1. Two Sum (Easy)
https://leetcode.com/problems/two-sum/
题目描述
    给定一个整数数组，已知  有且只有  两个数的和等于给定值，求这两个数的位置。
输入输出样例
    输入一个一维整数数组和一个目标值，输出是一个大小为 2 的一维数组，表示满足条件的两
    个数字的位置。
    Input: nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]
    在这个样例中，第 0 个位置的值 2 和第 1 个位置的值 7 的和为 9。
题解
    利用哈希表（python为字典）存储遍历过的值以及他们的位置，每次遍历到位置i的时候，查找哈希
    表里是否存在target-nums[i]，如存在，则说明这两个值和为target
"""

def twoSum(nums, target):
    hashMap=dict()
    ans=[]
    for i in range(len(nums)):
        num1=nums[i]
        num2=target-num1
        if num2 in hashMap:
            return [hashMap[num2],i]
        if num1 not in hashMap:
            hashMap[num1]=i
    return []


nums=[3,3]
target=6
ans=twoSum(nums,target)
print(ans)

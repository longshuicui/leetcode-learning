# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/4/23
@function:
368. 最大整除子集 (Medium)
https://leetcode-cn.com/problems/largest-divisible-subset/
给你一个由 无重复 正整数组成的集合 nums ，请你找出并返回其中最大的整除子集 answer ，子集中每一元素对 (answer[i], answer[j]) 都应当满足：
answer[i] % answer[j] == 0 ，或
answer[j] % answer[i] == 0
如果存在多个有效解子集，返回其中任何一个均可。

示例 1：
    输入：nums = [1,2,3]
    输出：[1,2]
    解释：[1,3] 也会被视为正确答案。
示例 2：
    输入：nums = [1,2,4,8]
    输出：[1,2,4,8]

题解：
    动态规划和最长递增子序列的长度差不多
    状态定义：dp[i]表示在输入数组nums升序排列下，以nums[i]为最大整数的 整除子集 的大小
    状态转移方程：枚举 j = 0...i-1的所有整数，如果nums[j]能整除nums[i]，说明nums[i]可以扩充
    初始化：由于nums[i]一定会选择，对于任意i=0...n-1，dp[i]=1
    因为返回的是一个列表而不是一个最大值， 所以还需要倒推回去，注意是任意两个都可以互相整除，
"""

def largestDivisibleSubset(nums):
    nums.sort()
    dp = [1] * len(nums)  # 保存当前子集的大小
    index, maxSize = 0, 1
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                dp[i] = max(dp[i], dp[j] + 1)
        if dp[i] > maxSize:
            maxSize = dp[i]
            index = i
    if maxSize == 1:
        return [nums[0]]
    res = []
    for i in range(index, -1, -1):
        if dp[i] == maxSize and nums[index] % nums[i] == 0:
            res.append(nums[i])
            index = i
            maxSize -= 1
    return res



nums=[4]
res=largestDivisibleSubset(nums)
print(res)




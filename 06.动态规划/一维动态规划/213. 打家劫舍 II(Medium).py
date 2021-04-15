# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/4/15
@function:
213. 打家劫舍 II (Medium)
https://leetcode-cn.com/problems/house-robber-ii/
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。
这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。
同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。

给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，能够偷窃到的最高金额。

示例：
    输入：nums = [2,3,2]
    输出：3
    输入：nums = [1,2,3,1]
    输出：4
    输入：nums = [0]
    输出：0
"""


def rob_(nums):
    dp=[0, nums[0]]
    for i in range(2, len(nums)+1):
        dp.append(max(dp[i-1], dp[i-2]+nums[i-1]))
    return dp[-1]

def rob(nums):
    if len(nums)==1:
        return nums[0]
    if len(nums)==2:
        return max(nums)
    a=rob_(nums[1:])
    b=rob_(nums[:-1])
    return max(a, b)

nums=[2,3,2]
res=rob(nums)
print(res)

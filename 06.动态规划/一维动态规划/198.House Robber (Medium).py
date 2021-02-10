# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/1
@function:
198. House Robber (Medium)
https://leetcode.com/problems/house-robber/
题目描述
    假如你是一个劫匪，并且决定抢劫一条街上的房子，每个房子内的钱财数量各不相同。如果
    你抢了两栋相邻的房子，则会触发警报机关。求在不触发机关的情况下最多可以抢劫多少钱。
输入输出样例
    输入是一个一维数组，表示每个房子的钱财数量；输出是劫匪可以最多抢劫的钱财数量。
    Input: [2,7,9,3,1]
    Output: 12
    在这个样例中，最多的抢劫方式为抢劫第 1、 3、 5 个房子。
题解
    创建数组dp，dp[i]表示抢劫到第i个房子时，可以抢劫的最大数量。对于dp[i]，最大数量有两种可能。
    一种是我们选择不抢劫这个房子，累计金额为dp[i-1]；一种是抢劫这个房子，累计金额为dp[i-2]+nums[i]
    状态转移方程：dp[i]=max(dp[i-1],nums[i-1]+dp[i-2])
"""


def rob(nums):
    if len(nums)==0: return 0
    dp=[0,nums[0]]
    for i in range(2,len(nums)+1):
        dp.append(max(dp[i-1],nums[i-1]+dp[i-2]))
    return dp[-1]


def robber(nums):
    a,b=0,0
    for i in range(len(nums)):
        a,b=max(b+nums[i], a), a
    return a




nums=[1,2,3,1]
cnt=rob(nums)


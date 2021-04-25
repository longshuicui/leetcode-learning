# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/4/25
@function:
https://leetcode-cn.com/problems/combination-sum-iv/
给你一个由 不同 整数组成的数组 nums ，和一个目标整数 target 。请你从 nums 中找出并返回总和为 target 的元素组合的个数。
题目数据保证答案符合 32 位整数范围。
示例 1：
    输入：nums = [1,2,3], target = 4
    输出：7
    解释：
        所有可能的组合为：
        (1, 1, 1, 1)
        (1, 1, 2)
        (1, 2, 1)
        (1, 3)
        (2, 1, 1)
        (2, 2)
        (3, 1)

    输入：nums = [9], target = 3
    输出：0

"""


def combinationSum4(nums, target):
    dp=[0]*(target+1)
    dp[0]=1 # 初始条件target为0时，只有什么数都不选这一种情况
    for i in range(1,target+1):
        for num in nums:
            if i>=num:
                dp[i]+=dp[i-num]
    return dp[-1]

nums=[1,2,3]
target=4
res=combinationSum4(nums, target)
print(res)

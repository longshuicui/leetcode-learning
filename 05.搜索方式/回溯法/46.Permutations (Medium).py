# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/1/30
@function:
46. Permutations  (Medium)
https://leetcode.com/problems/permutations/

题目描述
    给定一个 无重复数字 的整数数组，求其所有的排列方式。
输入输出样例
    输入是一个一维整数数组，输出是一个二维数组，表示输入数组的所有排列方式。
    Input: [1,2,3]
    Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,2,1], [3,1,2]]
    可以以任意顺序输出，只要包含了所有排列方式即可。

题解
    对于当前位置i，可以将之后的位置交换，然后处理位置i+1，直到最后一位。
    为防止每次遍历都要新建一个数组存储之前交换好的数字，利用回溯法，只
    对原数组进行修改，在递归完成后修改回来。
    python里面需要使用深拷贝
"""
from copy import deepcopy

def permute(nums):
    ans = []
    def backtracking(level):
        if level == len(nums) - 1:
            ans.append(deepcopy(nums)) # 这里需要使用深拷贝
            return
        for i in range(level, len(nums)):
            nums[i], nums[level] = nums[level], nums[i] # 修改当前节点状态
            backtracking(level + 1) # 递归子节点
            nums[i], nums[level] = nums[level], nums[i] # 回改当前节点状态
    backtracking(0)
    return ans


nums=[1,2,3]
ans=permute(nums)
print(ans)
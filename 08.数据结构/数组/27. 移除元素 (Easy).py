# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/4/19
@function:
27. 移除元素 (Easy)
https://leetcode-cn.com/problems/remove-element/
给你一个数组 nums和一个值 val，你需要 原地 移除所有数值等于val的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

示例：
    输入：nums = [3,2,2,3], val = 3
    输出：2, nums = [2,2]
    输入：nums = [0,1,2,2,3,0,4,2], val = 2
    输出：5, nums = [0,1,4,0,3]
"""

def removeElement(nums, val):
    slow, fast=0,0
    while fast<len(nums):
        if nums[fast]!=val:
            nums[slow]=nums[fast]
            fast+=1
            slow+=1
        else:
            fast+=1
    return slow


nums=[0,1,2,2,3,0,4,2]
val=2
res=removeElement(nums, val)
print(res)
print(nums)
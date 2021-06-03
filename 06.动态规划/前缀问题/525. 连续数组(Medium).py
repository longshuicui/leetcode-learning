# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/6/3
@function:
525. 连续数组 (Medium)
https://leetcode-cn.com/problems/contiguous-array/
给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。

示例 1:
    输入: nums = [0,1]
    输出: 2
    说明: [0, 1] 是具有相同数量0和1的最长连续子数组。
示例 2:
    输入: nums = [0,1,0]
    输出: 2
    说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。

"""


def findMaxLength(nums):
    """将0转换为-1，通过前缀和解决"""
    hashMap={0:-1}
    counter=ans=0
    for i, num in enumerate(nums):
        if num:
            counter+=1
        else:
            counter-=1
        if counter in hashMap:
            ans=max(ans, i-hashMap[counter])
        else:
            hashMap[counter]=i
    return ans



nums=[0,1,0]
res=findMaxLength(nums)
print(res)












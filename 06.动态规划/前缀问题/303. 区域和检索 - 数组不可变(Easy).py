# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/4/23
@function:
303. 区域和检索 - 数组不可变 (Easy)
https://leetcode-cn.com/problems/range-sum-query-immutable/
给定一个整数数组 nums，求出数组从索引i到j（i≤j）范围内元素的总和，包含i、j两点。

实现 NumArray 类：

NumArray(int[] nums) 使用数组 nums 初始化对象
int sumRange(int i, int j) 返回数组 nums 从索引i到j（i≤j）范围内元素的总和，包含i、j两点（也就是 sum(nums[i], nums[i + 1], ... , nums[j])）
"""

class NumArray:
    """遍历求和，时间复杂度O(n)"""
    def __init__(self, nums):
        self.arrays=nums

    def sumRange(self, left, right):
        res=0
        for i in range(left, right+1):
            res+=self.arrays[i]
        return res

class NumArrayAdvance:
    """sum[j]-sum[i-1]的结果即为[i, j]的加和，这里时间复杂度为O(1)
    记录了当前位置的前缀和（包含当前下标）
    """
    def __init__(self, nums):
        self.sum=[0]
        for num in nums:
            self.sum.append(num+self.sum[-1])

    def sumRange(self, left, right):
        res=self.sum[right+1]-self.sum[left-1+1]
        return res


nums=[-2, 0, 3, -5, 2, -1]
obj=NumArrayAdvance(nums)
res=obj.sumRange(0,5)
print(res)
# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/18
@function:
540. Single Element in a Sorted Array (Medium)
https://leetcode.com/problems/single-element-in-a-sorted-array/
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.
Follow up: Your solution should run in O(log n) time and O(1) space.
在时间复杂度为O(logn)和空间复杂度为O(1)的条件下找出只出现一次的数字
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Input: nums = [3,3,7,7,10,11,11]
Output: 10
因为是O(logn)的时间复杂度，不可以使用位操作，使用二分搜索来做
数组里面的数字要么出现一次，要么出现两次
"""


def singleNonDuplicate(nums):
    if len(nums) == 1:
        return nums[0]
    l,r=0, len(nums)-1
    while l<=r:
        if nums[l]!=nums[l+1]:
            return nums[l]
        if nums[r]!=nums[r-1]:
            return nums[r]
        l+=2
        r-=2
    return -1


nums=[3,3,7,7,10,11,11]
num=singleNonDuplicate(nums)
print(num)
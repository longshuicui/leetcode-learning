# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/18
@function:
154. Find Minimum in Rotated Sorted Array II (Hard)
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element.
The array may contain duplicates.
Input: [1,3,5]
Output: 1
Input: [2,2,2,0,1]
Output: 0
"""


def findMin(nums):
    start, end = 0, len(nums) - 1
    if nums[start] < nums[end]:  # 数组已经排好序，直接返回第一个元素
        return nums[start]
    while start<end:
        mid=start+(end-start)//2
        if nums[mid]>nums[end]:
            start=mid+1
        elif nums[mid]<nums[end]:
            end=mid
        else:
            end-=1
    return nums[start]


nums = [3,5,1]
res = findMin(nums)
print(res)

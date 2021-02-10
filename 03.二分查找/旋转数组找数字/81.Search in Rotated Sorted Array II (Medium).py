# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/1/27
@function:
81. Search in Rotated Sorted Array II (Medium)
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
题目描述
    一个原本 增序 的数组被 首尾相连 后按某个位置断开（如 [1,2,2,3,4,5] ! [2,3,4,5,1,2]，在第一
    位和第二位断开），我们称其为旋转数组。给定一个值，判断这个值是否存在于这个为旋转数组
    中。
输入输出样例
    输入是一个数组和一个值，输出是一个布尔值，表示数组中是否存在该值。
    Input: nums = [2,5,6,0,0,1,2], target = 0
    Output: true

题解
    二分查找思想。对于当前的中点，如果值小于右端，说明右边是排好序的；反之，说明左边是排好序的。如果目标值
    位于排好序的空间内， 可以对这个区间继续二分查找；反之对另外一个半区间进行二分查找。
"""


def search(nums, target):
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return True
        if nums[start] == nums[mid]:
            start += 1
        elif nums[mid] <= nums[end]:
            # 右区间是增序的
            if nums[mid] < target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1
        else:
            # 左边是增序的
            if nums[start] <= target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
    return False


nums = [1,0,1,1,1]
target = 0
r = search(nums, target)
print(r)

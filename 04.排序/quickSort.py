# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/18
@function:
"""


def quickSort(nums, low, high):
    if low >= high:
        return nums
    i, j = low, high
    pivot = nums[low]
    while i < j:
        while i < j and nums[j] >= pivot:  # 寻找基准右侧比基准小的数
            j -= 1
        nums[i] = nums[j]
        while i < j and nums[i] <= pivot:  # 寻找基准左侧比基准大的数
            i += 1
        nums[j] = nums[i]

    nums[j] = pivot
    quickSort(nums, low, i - 1)
    quickSort(nums, i + 1, high)
    return nums


nums = [1, 3, 2, 1]
nums = quickSort(nums, 0, len(nums) - 1)
print(nums)

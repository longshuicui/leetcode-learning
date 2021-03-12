# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/3/12
@function:
一个数组满足 2*nums[i]<nums[i+1]，给定一个数target，是否存在两个数满足a+b=target，若存在返回a,b
举例
nums=[1,4,9,21,48,120,256], target=52
返回 4， 48

要求， O(logn)
"""


def twoSum(nums, target):
    l, r = 0, len(nums) - 1
    maxValueIndex = findMaxValueIndex(nums, target, l, r)
    if maxValueIndex:
        minValue = target - nums[maxValueIndex]
        minValueIndex = findMinValueIndex(nums[:maxValueIndex], minValue, 0, maxValueIndex - 1)
        if minValueIndex:
            return [minValue, nums[maxValueIndex]]
    return None


def findMaxValueIndex(nums, target, l, r):
    while l <= r:
        mid = l + (r - l) // 2
        if 2 * target / 3 <= nums[mid] <= target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return None


def findMinValueIndex(nums, target, l, r):
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return None


nums = [1, 4, 9, 21, 48, 120, 256]
target = 52
ans = twoSum(nums, target)
print(ans)

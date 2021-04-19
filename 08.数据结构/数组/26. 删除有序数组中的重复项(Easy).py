# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/4/19
@function:
26. 删除有序数组中的重复项 (Easy)
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

示例：
    输入：nums = [1,1,2]
    输出：2, nums = [1,2]
    输入：nums = [0,0,1,1,1,2,2,3,3,4]
    输出：5, nums = [0,1,2,3,4]
"""


def removeDuplicates(nums):
    slow, fast = 0, 1
    while fast < len(nums):
        if nums[fast] == nums[slow]:
            fast += 1
        else:
            slow += 1
            nums[slow] = nums[fast]
            fast += 1
    return slow + 1


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
res = removeDuplicates(nums)
print(res)
print(nums)

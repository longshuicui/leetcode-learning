# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :  2021/02/25
@function:
75. Sort Colors (Medium)
https://leetcode.com/problems/sort-colors/
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
Example 3:

Input: nums = [0]
Output: [0]
Example 4:

Input: nums = [1]
Output: [1]
"""


def sortColors(nums):
    left, right, current = 0, len(nums) - 1, 0
    while current <= right:
        if nums[current] == 0:
            nums[current], nums[left] = nums[left], nums[current]
            current += 1
            left += 1
        elif nums[current] == 1:
            current += 1
        elif nums[current] == 2:
            nums[right], nums[current] = nums[current], nums[right]
            right -= 1


nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)
print(nums)

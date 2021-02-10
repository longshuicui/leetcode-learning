# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/7
@function:
128. Longest Consecutive Sequence (Hard)
https://leetcode.com/problems/longest-consecutive-sequence/
题目描述
    给定一个整数数组，求这个数组中的数字可以组成的  最长连续序列  有多长。
输入输出样例
    输入一个整数数组，输出一个整数，表示连续序列的长度。
    Input: [100, 4, 200, 1, 3, 2]
    Output: 4
    在这个样例中，最长连续序列是 [1,2,3,4]。
题解
    将所有的数字都放到一个哈希表，然后不断从哈希表中任意取一个值，
"""


def longestConsecutiveBrute(nums):
    """暴力搜索，取最长连续子序列长度，时间复杂度高，最差 O(n**3)"""
    longest_streak = 0
    for num in nums:
        current_num = num
        current_streak = 1
        while current_num + 1 in nums:
            current_num += 1
            current_streak += 1
        longest_streak = max(longest_streak, current_streak)
    return longest_streak


def longestConsecutiveHashMap(nums):
    """对暴力搜索的优化，创建一个数组，在O(1)的时间复杂度下去查找"""
    longest_streak = 0
    num_set = set(nums)
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            longest_streak = max(longest_streak, current_streak)
    return longest_streak


def longestConsecutiveSort(nums):
    """预先排序，然后找到连续子序列。时间复杂度是排序的复杂度，但是这个不能AC"""
    if not nums:
        return 0
    nums.sort()
    longest_streak = 1
    current_streak = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[1 - 1]:
            if nums[i] == nums[i - 1] + 1:
                current_streak += 1
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1
    return max(longest_streak, current_streak)


nums = [1, 2, 0, 1]
ans = longestConsecutiveHashMap(nums)
print(ans)

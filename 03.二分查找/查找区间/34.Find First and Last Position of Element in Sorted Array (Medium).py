# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/1/27
@function:
34. Find First and Last Position of Element in Sorted Array (Medium)
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
题目描述
    给定一个 增序 的整数数组和一个值，查找该值 第一次 和 最后一次 出现的位置。
输入输出样例
    输入是一个数组和一个值，输出为该值第一次出现的位置和最后一次出现的位置（从 0 开
    始）；如果不存在该值，则两个返回值都设为-1。
    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]
    数字 8 在第 3 位第一次出现，在第 4 位最后一次出现

题解
    实现python里的index函数，左闭右开/左闭右闭
"""


def lower_bound(nums, target):
    l,r=0, len(nums)
    while l<r:
        mid = l + (r - l) // 2
        if nums[mid]>=target:
            r=mid
        else:
            l=mid+1
    return l


def upper_bound(nums, target):
    l,r=0, len(nums)
    while l<r:
        mid = l + (r - l) // 2
        if nums[mid]>target:
            r=mid
        else:
            l=mid+1
    return l


def searchRange(nums, target):
    if len(nums)==0:
        return [-1, -1]
    lower=lower_bound(nums, target)
    upper=upper_bound(nums, target)-1 # 这里需要减1, 因为过程右边界是取不到的，左闭右开

    if lower==len(nums) or nums[lower]!=target:
        return [-1,-1]
    return [lower, upper]



nums = [1,1,2,2,2]
target = 2
r=searchRange(nums, target)
print(r)
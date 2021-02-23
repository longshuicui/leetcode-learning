# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/1/27
@function:
215. Kth Largest Element in an Array (Medium)
https://leetcode.com/problems/kth-largest-element-in-an-array/
题目描述
    在一个  未排序  的数组中，找到第 k 大的数字。
输入输出样例
    输入一个数组和一个目标值 k，输出第 k 大的数字。题目默认一定有解。
    Input: [3,2,1,5,6,4] and k = 2
    Output: 5

题解
    快速选择   一半用于求解 k-th element 问题，可以在 O(n)时间复杂度，O(1)空间复杂度完成求解。
    快速选择和快速排序相似，只需要找到第K大的值即可，不需要左右进行排序，。
    快速选择需要打乱数组，否则最坏情况下时间复杂度为 O(n**2)
"""


def quickSelection(nums, l, r):
    i, j = l + 1, r
    while True:
        while i < r and nums[i] <= nums[l]:
            i += 1
        while l < j and nums[j] >= nums[l]:
            j -= 1
        if i >= j:
            break
        nums[i], nums[j] = nums[j], nums[i]
    nums[l], nums[j] = nums[j], nums[l]
    return j


def findKthLargest(nums, k):
    l, r = 0, len(nums) - 1
    target = len(nums) - k
    while l < r:
        mid = quickSelection(nums, l, r) # 相当于快排，不断移动基准点，如果目标值等于基准点就返回基准值
        if mid == target:
            return nums[mid]
        if mid < target:
            l = mid + 1
        else:
            r = mid - 1
    return nums[l]


def quickSort(nums, left, right):
    if left>=right:
        return nums
    pivot=nums[left]
    i, j = left, right
    while i<j:
        while i<j and nums[i]<=pivot: # 找到pivot左边比pivot大的值
            i+=1
        nums[j]=nums[i]
        while i<j and nums[j]>=pivot: # 找到pivot右边比pivot小的值
            j-=1
        nums[i]=nums[j]
        # nums[i], nums[j]=nums[j], nums[i]
    nums[j]=pivot
    quickSort(nums, left, i-1)
    quickSort(nums, i+1, right)
    return nums




nums = [3, 2, 1, 5, 6, 4]
# k = 3
# r = findKthLargest(nums, k)
# print(r)

nums=quickSort(nums, 0, len(nums)-1)
print(nums)

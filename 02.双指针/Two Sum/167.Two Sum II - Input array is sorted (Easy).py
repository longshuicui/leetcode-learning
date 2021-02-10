# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/1/26
@function:
167.Two Sum II - Input array is sorted (Easy)
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
题目描述
    在一个  增序  的整数数组里找到两个数，使它们的和为给定值。已知有且只有一对解。
输入输出样例
    输入是一个数组（numbers）和一个给定值（target）。输出是两个数的位置，   从 1 开始计数。
    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]
    在这个样例中，第一个数字（2）和第二个数字（7）的和等于给定值（9）。

策略：
    如果两个指针指向元素的和等于定值，返回结果。如果两个指针指向元素的和小于给定值，左边的指针右移；
    如果两个指针指向元素的和大于定值，右边的指针左移

"""


def twoSum(numbers, target):
    l,r=0, len(numbers)-1
    while l<r:
        s=numbers[l]+numbers[r]
        if s == target:
            break
        if s<target:
            l+=1
        else:
            r-=1
    return [l+1, r+1]


numbers = [2,7,11,15]
target = 9
res=twoSum(numbers, target)
print(res)

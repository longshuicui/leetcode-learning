# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/3
@function:
136. Single Number (Easy)
https://leetcode.com/problems/single-number/
题目描述
    给定一个整数数组，这个数组里只有一个数次出现了一次，其余数字出现了两次，求这个只
    出现一次的数字。
输入输出样例
    输入是一个一维整数数组，输出是该数组内的一个整数。
    Input: [4,1,2,1,2]
    Output: 4
题解
    我们可以利用 x ^ x = 0 和 x ^ 0 = x 的特点，将数组内所有的数字进行按位异或。出现两次
    的所有数字按位异或的结果是 0， 0 与出现一次的数字异或可以得到这个数字本身。
    0和任一数字异或得到这个数字本身
    数字与自身异或得0
"""

def singleNumber(nums):
    ans=0
    for num in nums:
        ans^=num
    return ans

nums=[4,1,2,1,2]
ans=singleNumber(nums)
print(ans)

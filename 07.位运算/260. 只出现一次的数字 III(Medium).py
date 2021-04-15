# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/4/14
@function:
260. 只出现一次的数字 III (Medium)
https://leetcode-cn.com/problems/single-number-iii/
给定一个整数数组 nums，其中 恰好 有 两个 元素只出现一次，其余所有元素均出现两次。
找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。
时间复杂度O(n)， 空间复杂度O(1)
示例：
    输入：nums = [1,2,1,3,2,5]
    输出：[3,5]
    解释：[5, 3] 也是有效的答案。

    输入：nums = [-1,0]
    输出：[-1,0]
题解：
    单个数字出现一次，采用异或操作，现在是两个数字只出现一次。
    将所有的数字分为两组，使两个只出现一次的数字出现在不同的组中，相同的数出现在相同的组中
    对这两个组分别进行异或操作，就可以获得这两个数字
    先对所有数字进行异或，得到两个出现一次的数字的异或值，在异或结果中找到任意为1的位置，
    根据这一位对数组进行分组，在每个组内进行异或操作，得到两个数字
"""

import functools

def singleNumber(nums):
    ret=functools.reduce(lambda x,y:x^y, nums)
    div=1
    while div & ret == 0:
        div<<=1
    a,b=0,0
    for n in nums:
        if n&div:
            a^=n
        else:
            b^=n
    return [a,b]


nums=[1,2,1,3,2,5]
res=singleNumber(nums)
print(res)

# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/4/12
@function:
179. 最大数 (Medium)
给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

示例：
    输入：nums = [10,2]
    输出："210"
    输入：nums = [3,30,34,5,9]
    输出："9534330"
    输入：nums = [1]
    输出："1"

题解：
    按照最高位，进行排序， 贪心思想，每一位都取最大的
    开头数字不相同，直接按照排序结果进行拼接就可以
    如果开头数字相同，就需要比较如何拼接才能保证数字最大
"""
import functools


def largestNumber(nums):
    nums = list(map(str, nums))
    nums.sort(key=functools.cmp_to_key(lambda x, y: 1 if x + y < y + x else -1))
    ans = "".join(nums)
    if ans[0]=="0":
        ans="0"
    return ans


nums = [0, 0]
res = largestNumber(nums)
print(res)

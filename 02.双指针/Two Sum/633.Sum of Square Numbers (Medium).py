# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :  2021/02/16
@function:
633. Sum of Square Numbers (Medium)
https://leetcode.com/problems/sum-of-square-numbers/
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.
Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
"""
import math
def judgeSquareSum(c):
    l, r = 0, c if c <= 2 else int(math.sqrt(c)) + 1
    while l <= r:
        s = l * l + r * r
        if s > c:
            r -= 1
        elif s < c:
            l += 1
        else:
            return True
    return False


c=2
res=judgeSquareSum(c)
print(res)
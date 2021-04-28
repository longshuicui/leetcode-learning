# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/4/28
@function:
633. 平方数之和 (Medium)
https://leetcode-cn.com/problems/sum-of-square-numbers/
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。
示例 1：
    输入：c = 5
    输出：true
    解释：1 * 1 + 2 * 2 = 5

示例 2：
    输入：c = 3
    输出：false

示例 3：
    输入：c = 4
    输出：true

示例 4：
    输入：c = 2
    输出：true

示例 5：
    输入：c = 1
    输出：true

"""
import math
def judgeSquareSum(c):
    left, right=0, int(math.sqrt(c))+1
    while left<=right:
        ans=left**2+right**2
        if ans==c:
            return True
        elif ans<c:
            left+=1
        else:
            right-=1
    return False

c=3
res=judgeSquareSum(c)
print(res)


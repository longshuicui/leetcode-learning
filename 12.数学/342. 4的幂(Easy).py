# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/5/31
@function:
342. 4的幂 (Easy)
给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 true ；否则，返回 false 。
整数 n 是 4 的幂次方需满足：存在整数 x 使得 n == 4^x

示例 1：
    输入：n = 16
    输出：true
示例 2：
    输入：n = 5
    输出：false
示例 3：
    输入：n = 1
    输出：true

"""

import math


def isPowerOfFour(n):
    if n<=0:
        return False
    x=math.log(n, 4)
    if x==int(x):
        return True
    return False

n=256
res=isPowerOfFour(n)
print(res)

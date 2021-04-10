# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :  2021/04/10
@function:
263. 丑数 (Easy)
https://leetcode-cn.com/problems/ugly-number/
给你一个整数 n ，请你判断 n 是否为 丑数 。如果是，返回 true ；否则，返回 false 。

丑数 就是只包含质因数 2、3 和/或 5 的正整数。

示例 1：
    输入：n = 6
    输出：true
    解释：6 = 2 × 3
示例 2：
    输入：n = 8
    输出：true
    解释：8 = 2 × 2 × 2
示例 3：
    输入：n = 14
    输出：false
    解释：14 不是丑数，因为它包含了另外一个质因数 7 。

"""


def isUgly(n):
    if n<=0:
        return False
    for factor in [2,3,5]:
        while n%factor==0:
            n//=factor
    return n==1

n=14
res=isUgly(n)
print(res)
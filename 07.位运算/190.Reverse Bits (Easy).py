# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/3
@function:
190. Reverse Bits (Easy)
https://leetcode.com/problems/reverse-bits/
题目描述
    给定一个十进制整数，输出它在二进制下的翻转结果。
输入输出样例
    输入和输出都是十进制整数。
    Input: 43261596 (00000010100101000001111010011100)
    Output: 964176192 (00111001011110000010100101000000)
题解
    使用算术 左移 和 右移，可以很轻易地实现二进制的翻转。
"""


def reverseBits(n):
    ans = 0
    for i in range(32):
        ans = ans << 1
        ans += n & 1
        n >>= 1
    return ans

n=4
ans=reverseBits(n)
print(ans)
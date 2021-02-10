# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/3
@function:
461. Hamming Distance (Easy)
https://leetcode.com/problems/hamming-distance/
题目描述
    给定两个十进制数字，求它们二进制表示的汉明距离（Hamming distance，即不同位的个数）。
输入输出样例
    输入是两个十进制整数，输出是一个十进制整数，表示两个输入数字的汉明距离。
    Input: x = 1, y = 4
    Output: 2
    在这个样例中， 1 的二进制是 0001， 4 的二进制是 0100，一共有两位不同。
题解
    对两个数进行按位  异或  操作，统计有多少个 1 即可。
"""
"""
按位运算
& 按位与运算 当对应的二进位都为1时，结果为1
| 按位或运算  当对应的二进位至少有一个1时，结果为1
^ 按位异或运算，当对应的二进位不同时，结果为1
~ 按位取反运算 把1变为0，把0变为1
<< 左移运算符
>> 右移运算符
"""


def hammingDistance(x,y):
    diff=x^y
    ans=0
    while diff:
        ans+=diff & 1
        diff>>=1
        print(ans, diff)
    return ans


x=1
y=4
ans=hammingDistance(x,y)
print(ans)
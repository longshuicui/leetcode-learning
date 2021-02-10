# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/7
@function:
205. Isomorphic Strings (Easy)
https://leetcode.com/problems/isomorphic-strings/
题目描述
    判断两个字符串是否同构。同构的定义是，可以通过把一个字符串的某些相同的字符转换成
    另一些相同的字符，使得两个字符串相同，且两种不同的字符不能够被转换成同一种字符。
输入输出样例
    输入两个字符串，输出一个布尔值，表示两个字符串是否满足条件。
    Input: s = "paper", t = "title"
    Output: true
    在这个样例中，通过把 s 中的 p、 a、 e、 r 字符转换成 t、 i、 l、 e 字符，可以使得两个字符串相同，
题解
    记录两个字符串每个位置的字符第一次出现的位置，如果两个字符串中相同位置的字符与它们第一次出现的
    位置一样，那么这两个字符串同构。
    举例：对于paper和title，假设遍历到第三个字符p和t，发现他们第一次出现的位置都在第一个字符，则说明目前
    的位置满足同构
"""

def isIsomorphic(s, t):
    s_first_index=dict()
    t_first_index=dict()
    if len(s)!=len(t):
        return False
    for i in range(len(s)):
        if s[i] not in s_first_index:
            s_first_index[s[i]]=i+1
        if t[i] not in t_first_index:
            t_first_index[t[i]]=i+1
        if s_first_index[s[i]]!=t_first_index[t[i]]:
            return False
    return True


s="egg"
t="add"
ans=isIsomorphic(s,t)
print(ans)


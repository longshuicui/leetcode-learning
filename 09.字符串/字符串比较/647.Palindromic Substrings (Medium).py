# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/7
@function:
647. Palindromic Substrings (Medium)
https://leetcode.com/problems/palindromic-substrings/
题目描述
    给定一个字符，求其有多少个回文子字符串。回文的定义是左右对称。
输入输出样例
    输入是一个字符串，输出一个整数，表示回文子字符串的数量。
    Input: "aaa"
    Output: 6
    六个回文子字符串分别是 ["a","a","a","aa","aa","aaa"]。
题解
    从每个字符开始，向左向右延长，判断存在多少以当前位置为中轴的同文子字符串
    回文数，就需要用到双指针，找出所有的回文数，每个位置遍历，从中间向四周发散
"""
def countSubstrings(s):
    counts=0
    for i in range(len(s)):
        counts+=extendSubstrings(s,i,i) # 奇数长度
        counts+=extendSubstrings(s,i,i+1) # 偶数长度
    return counts


def extendSubstrings(s,l,r):
    count=0
    while l>=0 and r<len(s) and s[l]==s[r]:
        l-=1
        r+=1
        count+=1
    return count



s="aaa"
count=countSubstrings(s)
print(count)

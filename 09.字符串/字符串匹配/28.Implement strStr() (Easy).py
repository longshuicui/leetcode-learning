# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/7
@function:
28. Implement strStr() (Easy)
https://leetcode.com/problems/implement-strstr/
题目描述
    判断一个字符串是不是另一个字符串的子字符串，并返回其位置。
输入输出样例
    输入一个母字符串和一个子字符串，输出一个整数，表示子字符串在母字符串的位置，若不
    存在则返回-1。
    Input: haystack = "hello", needle = "ll"
    Output: 2
题解
"""

def strStr(haystack, needle):
    pos=haystack.find(needle)
    return pos

haystack="hello"
needle="ll"
pos=strStr(haystack, needle)
print(pos)

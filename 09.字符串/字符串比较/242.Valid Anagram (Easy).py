# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/7
@function:
242. Valid Anagram (Easy)
https://leetcode.com/problems/valid-anagram/
题目描述
    判断两个字符串包含的字符是否 完全相同 （不考虑顺序）。
输入输出样例
    输入两个字符串，输出一个布尔值，表示两个字符串是否满足条件。
    Input: s = "anagram", t = "nagaram"
    Output: true
题解
    使用哈希表或者数组统计两个字符串中每个字符出现的 频次 ，若频次相同 则说明他们包含的字符完全相同
"""
def isAnagram(s,t):
    if len(s)!=len(t):
       return False
    counts={chr(i):0 for i in range(97,97+26)}
    for i in range(len(s)):
       counts[s[i]]+=1
       counts[t[i]]-=1
    for c in counts:
        if counts[c]:
            return False
    return True





s = "anagram"
t = "nagaram"
ans=isAnagram(s,t)
print(ans)
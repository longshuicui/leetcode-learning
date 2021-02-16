# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/1/26
@function:
76. Minimum Window Substring (Hard)
https://leetcode.com/problems/minimum-window-substring/
题目描述
    给定两个字符串 S 和 T，求 S 中包含 T 所有字符的  最短连续子字符串  的长度，同时要求时间
    复杂度不得超过 O(n)。
输入输出样例
    输入是两个字符串 S 和 T，输出是一个 S 字符串的子串。
    Input: S = "ADOBECODEBANC", T = "ABC"
    Output: "BANC"
    在这个样例中， S 中同时包含一个 A、一个 B、一个 C 的最短子字符串是“BANC”。
题解
    滑动窗口求解。
    l和r都是从左到右
"""


def minWindow(s,t):
    if not t or not s:
        return ""
    counts={}
    for c in t:
        counts[c]=counts.get(c,0)+1
    formed=0
    l,r=0,0
    windowCounts={}
    ans=float("inf"),None,None
    while r<len(s):
        c=s[r]
        windowCounts[c]=windowCounts.get(c,0)+1
        if c in counts and windowCounts[c]==counts[c]:
            formed+=1
        while l<=r and formed==len(counts): # 都出现了移动左指针
            c=s[l]
            if r-l+1 < ans[0]:
                ans=(r-l+1,l,r)
            windowCounts[c]-=1
            if c in counts and windowCounts[c]<counts[c]:
                formed-=1
            l+=1
        r+=1
    return "" if ans[0]==float("inf") else s[ans[1]:ans[2]+1]


S = "ADOBECODEBANC"
T = "ABC"
t=minWindow(S,T)
print(t)
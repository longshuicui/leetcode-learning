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


def minWindow(S, T):
    chars={}
    flag={}
    for i in range(len(T)):
        flag[T[i]]=True
        chars[T[i]]=chars.get(T[i],0)+1

    # 滑动窗口, 不断更改统计数据
    cnt, l, min_l = 0, 0, 0
    min_size=len(S)+1

    for r in range(len(S)):
        # 判断是否在T种
        if S[r] in flag:
            chars[S[r]]-=1
            if chars[S[r]]>=0:
                cnt+=1
            # 最短子串可以包含T以外的字符，所以
            while cnt==len(T):
                if r-l+1<min_size:
                    min_l=l
                    min_size=r-l+1
                chars[S[l]]+=1
                if flag[S[l]] and chars[S[l]]>0:
                    cnt-=1
                l+=1
    if min_size> len(S):
        return ""
    return S[min_l,min_l+min_size]






S = "ADOBECODEBANC"
T = "ABC"
t=minWindow(S,T)
print(t)
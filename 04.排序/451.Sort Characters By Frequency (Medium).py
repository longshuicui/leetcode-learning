# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :  2021/02/25
@function:
451. Sort Characters By Frequency (Medium)
https://leetcode.com/problems/sort-characters-by-frequency/
Given a string, sort it in decreasing order based on the frequency of characters.
Input:
"tree"

Output:
"eert"
"""

def frequencySort(s):
    counts={}
    for c in s:
        counts[c]=counts.get(c,0)+1
    counts=sorted(counts.items(),key=lambda x:x[1], reverse=True)
    new=""
    for c, count in counts:
        new+=c*count
    return new

s="Aabb"
res=frequencySort(s)
print(res)
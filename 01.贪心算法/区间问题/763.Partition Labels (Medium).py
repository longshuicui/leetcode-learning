# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :  2021/02/15
@function:
763. Partition Labels (Medium)
https://leetcode.com/problems/partition-labels/
A string S of lowercase English letters is given.
We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
"""

def partitionLabels(s):
    # 统计每个字母出现的始末位置，变成区间问题
    last={c:i for i,c in enumerate(s)}
    j=anchor=0
    ans=[]
    for i,c in enumerate(s):
        j=max(j,last[c])
        if i==j:
            ans.append(i-anchor+1)
            anchor=i+1
    return ans

s="ababcbacadefegdehijhklij"
res=partitionLabels(s)
print(res)

# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/2
@function:
1143. Longest Common Subsequence (Medium)
https://leetcode.com/problems/longest-common-subsequence/
题目描述
    给定两个字符串，求它们最长的公共子序列长度。
输入输出样例
    输入是两个字符串，输出是一个整数，表示它们满足题目条件的长度。
    Input: text1 = "abcde", text2 = "ace"
    Output: 3
    在这个样例中，最长公共子序列是“ace”。

题解
    建立一个二维数组dp，其中dp[i][j]表示到第一个字符串位置i为止，到第二个字符串位置j为止，最长的公共子序列长度
"""
def longestCommonSubsequence(text1, text2):
    m,n=len(text1),len(text2)
    dp=[[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if text1[i-1]==text2[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]

text1="abc"
text2="abc"
res=longestCommonSubsequence(text1, text2)
print(res)
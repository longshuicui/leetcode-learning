# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/3
@function:
72. Edit Distance (Hard)
https://leetcode.com/problems/edit-distance/
题目描述
    给定两个字符串，已知你可以删除、替换和插入任意字符串的任意字符，求最少编辑几步可
    以将两个字符串变成相同。
输入输出样例
    输入是两个字符串，输出是一个整数，表示最少的步骤。
    Input: word1 = "horse", word2 = "ros"
    Output: 3
    在这个样例中，一种最优编辑方法是（1） horse -> rorse （2） rorse -> rose（3） rose -> ros。
题解
    类似于1143题，使用一个二维数组dp[i][j]，表示将第一个字符串到位置i为止，和第二个字符串到位置j为止，
    最多需要几步编辑。
    当第i位和第j位对应的字符相同时，dp[i][j]等于dp[i-1][j-1]
    当两者对应的字符不同时，修改的消耗是dp[i][j]等于dp[i-1][j-1]+1
    插入i位置/删除j位置消耗是dp[i][j-1]+1
    插入j位置/删除i位置消耗是dp[i-1][j]+1
"""
def minDistance(word1, word2):
    m,n=len(word1), len(word2)
    dp=[[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0:
                dp[i][j]=j # 字符串1是空，编辑距离就是字符串2的长度
            elif j==0:
                dp[i][j]=i # 同理，字符串2是空，编辑距离就是字符串1的长度
            else:
                dp[i][j]=min(dp[i-1][j-1] if word1[i-1]==word2[j-1] else dp[i-1][j-1]+1,
                             min(dp[i][j-1]+1, dp[i-1][j]+1))
    return dp[m][n]


word1="horse"
word2="ros"
res=minDistance(word1, word2)
print(res)
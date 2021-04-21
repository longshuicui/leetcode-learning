# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/2
@function:
91. Decode Ways (Medium)
https://leetcode.com/problems/decode-ways/
题目描述
    已知字母 A-Z 可以表示成数字 1-26。给定一个数字串，求有多少种不同的字符串等价于这个数字串.
输入输出样例
    输入是一个由数字组成的字符串，输出是满足条件的解码方式总数。
    Input: "226"
    Output: 3
    在这个样例中，有三种解码方式： BZ(2 26)、 VF(22 6) 或 BBF(2 2 6)。
题解
    动态规划
    当数字0或者相邻两个数字大于26时，需要有不同的状态转移方程
    dp[n]代表翻译长度为n个字符的字符串的方法总数。由于数字可能出现0，0不能翻译成任何字母，所以出现0要跳过。
    dp[0]代表空字符串，只有一种翻译方法，所以dp[0]=1，dp[1]需要考虑原字符串是否是0开头的，如果是0开头的，
    dp[1]=0；如果不是0，dp[1]=1。
    状态转移方程是：
    dp[i]+=dp[i-1] (1<=s[i-1:i]<=9)
    dp[i]+=dp[i-2] (10<=s[i-2:i]<=26)
    最终结果是dp(n)
"""


def numDecodings(s):
    if len(s)==0:
        return 0
    dp=[0]*(len(s)+1)
    dp[0]=1
    if s[:1]=="0":
        dp[1]=0
    else:
        dp[1]=1
    for i in range(2,len(s)+1):
        if s[i-1:i]!="0":
            if 1<=int(s[i-1:i])<=9:
                dp[i]=dp[i-1]
        if 10<=int(s[i-2:i])<=26:
            dp[i]+=dp[i-2]
    return dp[len(s)]


def numDecodings_(s):
    # 状态只与 dp[i-2] dp[i-1] dp[i]有关
    n=len(s)
    dp=[1]+[0]*n
    for i in range(1, n+1):
        if s[i-1]!="0": # 考虑一个数字的情况
            dp[i]+=dp[i-1]
        if i>1 and s[i-2]!="0" and int(s[i-2:i])<=26: # 两个数字的情况
            dp[i]+=dp[i-2]
    return dp[-1]




s="226"
cnt=numDecodings_(s)
print(cnt)


















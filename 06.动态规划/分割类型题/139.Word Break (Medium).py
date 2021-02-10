# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/2
@function:
139. Word Break (Medium)
https://leetcode.com/problems/word-break/
题目描述
    给定一个字符串和一个字符串集合，求是否存在一种分割方式，使得原字符串分割后的子字
    符串都可以在集合内找到。
输入输出样例
    Input: s = "applepenapple", wordDict = ["apple", "pen"]
    Output: true
    在这个样例中，字符串可以被分割为 [“apple” ,“pen” ,“apple” ]
题解
    类似于完全平方分割问题，分割条件由集合内的字符串决定，因此在考虑每个分割位置时，需要遍历字符串集合。
    以确定当前位置是否可以成功分割。对于位置0，需要初始化为真
"""
def wordBreak(s, wordDict):
    dp=[False]*(len(s)+1)
    dp[0]=True # 初始位置初始化为真
    for i in range(1,len(s)+1):
        for word in wordDict:
            if i>=len(word) and s[i-len(word):i]==word:
                dp[i]=dp[i] or dp[i-len(word)]
    return dp[len(s)]


s = "leetcode"
wordDict = ["leet", "code"]
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
res=wordBreak(s, wordDict)
print(res)
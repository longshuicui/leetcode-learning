# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/7
@function:
696. Count Binary Substrings (Easy)
https://leetcode.com/problems/count-binary-substrings/
题目描述
    给定一个 0-1 字符串，求有多少非空子字符串的  0 和 1  数量相同。
输入输出样例
    输入是一个字符串，输出一个整数，表示满足条件的子字符串的数量。
    Input: "00110011"
    Output: 6
    在这个样例中，六个 0 和 1 数量相同的子字符串是 ["0011","01","1100","10","0011","01"]。
题解
    从左往右遍历数组，记录和当前位置数字相同且连续的长度，以及其之前连续的不同数字的长度。
"""

def countBinarySubstrings(s):
    pre=0
    cur=1
    count=0
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
          cur+=1
        else:
            pre=cur
            cur=1
        if pre>=cur:
            count+=1
    return count


s="00110011"
c=countBinarySubstrings(s)
print(c)
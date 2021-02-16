# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :  2021/02/16
@function:
524. Longest Word in Dictionary through Deleting (Medium)
https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/
删除一些字母，可以形成字典里的最长的单词，若不存在则返回空字符串
"""

def findLongestWord(s, d):
    d.sort()
    maxLong=0
    longestWord=""
    for word in d:
        l,r=0,0
        while l<len(s) and r<len(word):
            if s[l]==word[r]:
                l+=1
                r+=1
            else:
                l+=1
        if r==len(word) and len(word)>maxLong:
            maxLong=len(word)
            longestWord=word
    return longestWord


s = "abpcplea"
d = ["c","b","a"]
res=findLongestWord(s,d)
print(res)
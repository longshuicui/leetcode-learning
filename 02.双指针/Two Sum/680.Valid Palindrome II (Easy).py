# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :  2021/02/16
@function:
680. Valid Palindrome II (Easy)
https://leetcode.com/problems/valid-palindrome-ii/
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
"""

def validPalindrome(s):
    l,r=0, len(s)-1
    while l<=r:
        if s[l]==s[r]:
            l+=1
            r-=1
        else:
            tmp1=s[:l]+s[l+1:]
            tmp2=s[:r]+s[r+1:]
            return tmp1==tmp1[::-1] or tmp2==tmp2[::-1]
    return True


s="aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
res=validPalindrome(s)
print(res)
# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/5/26
@function:
1190. 反转每对括号间的子串 (Medium)
https://leetcode-cn.com/problems/reverse-substrings-between-each-pair-of-parentheses/
给出一个字符串 s（仅含有小写英文字母和括号）。
请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。
注意，您的结果中 不应 包含任何括号。
示例 1：
    输入：s = "(abcd)"
    输出："dcba"
示例 2：
    输入：s = "(u(love)i)"
    输出："iloveu"
示例 3：
    输入：s = "(ed(et(oc))el)"
    输出："leetcode"
示例 4：
    输入：s = "a(bcdefghijkl(mno)p)q"
    输出："apmnolkjihgfedcbq"
"""

def reverseParentheses(s):
    # 统计下左括号的个数/位置/长度
    stack=[]
    s_=""
    for i in range(len(s)):
        if s[i]=="(":
            stack.append(s_)
            s_=""
        elif s[i]==")":
            i,j=0, len(s_)-1
            s_=list(s_)
            while i<=j:
                s_[i],s_[j]=s_[j],s_[i]
                i+=1
                j-=1
            s_=stack.pop()+"".join(s_)
        else:
            s_+=s[i]
    return s_


s="(ed(et(oc))el)"
res=reverseParentheses(s)
print(res)




















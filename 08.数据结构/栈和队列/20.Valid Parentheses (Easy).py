# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/4
@function:
20. Valid Parentheses (Easy)
https://leetcode.com/problems/valid-parentheses/
题目描述
    给定一个只由左右原括号、花括号和方括号组成的字符串，求这个字符串是否合法。合法的
    定义是每一个类型的左括号都有一个右括号一一对应，且括号内的字符串也满足此要求。
输入输出样例
    输入是一个字符串，输出是一个布尔值，表示字符串是否合法。
    Input: "{[]}()"
    Output: true
题解
    括号匹配典型用栈来实现。从左往右遍历，每当遇到左括号便放入栈内，遇到右括号则判断
    和栈顶的括号是否为同一类型，是则从栈内取出左括号，否则说明字符串不合法
"""


class Stack:

    def __init__(self):
        """初始化栈为一个空列表"""
        self.items = []

    def isEmpty(self):
        """判断栈是否为空，返回bool值"""
        return len(self.items) == 0

    def peek(self):
        """返回栈顶元素,也就是最后一个元素"""
        return self.items[-1]

    def size(self):
        """返回栈的大小"""
        return len(self.items)

    def push(self, item):
        """将新的元素堆进栈里面。入栈"""
        self.items.append(item)

    def pop(self):
        """出栈"""
        return self.items.pop()


def isValid(s):
    stack=[]
    for i in range(len(s)):
        if s[i]=="{" or s[i]=="[" or s[i]=="(":
            stack.append(s[i])
        else:
            if len(stack)==0:
                return False
            c=stack[-1]
            if (s[i]=="}" and c=="{") or (s[i]=="]" and c=="[") or (s[i]==")" and c=="("):
                stack.pop()
            else:
                return False
    return True if len(stack)==0 else False

s="{"
res=isValid(s)
print(res)

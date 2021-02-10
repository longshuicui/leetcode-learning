# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/1
@function:
126. Word Ladder II (Hard)
https://leetcode.com/problems/word-ladder-ii/
题目描述
    给定一个起始字符串和一个终止字符串，以及一个单词表，求是否可以将起始字符串每次改
    一个字符，直到改成终止字符串，且所有中间的修改过程表示的字符串都可以在单词表里找到。
    若存在，输出需要修改次数最少的所有更改方式。
输入输出样例
    输入是两个字符串，输出是一个二维字符串数组，表示每种字符串修改方式。
    Input: beginWord = "hit", endWord = "cog",
    wordList = ["hot","dot","dog","lot","log","cog"]
    Output:
    [["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]]

题解
    将起始字符串、终止字符串、以及字典表里的所有单词都想象成节点。若两个字符串只有一个字符不同，那么他们相连。
    输出修改次数最少的所有修改方式，可以使用广度优先搜索，求起始节点到终止节点的最短距离。
    从起始节点和终止节点分别进行广度优先搜索，可以减少搜索的总节点数
    搜索结束后，通过 回溯法 重建所有可能的路径
"""
from collections import deque


def findLadders(beginWord:str, endWord:str,wordList:list):
    ans=[]
    wordMap={}
    levelMap={}
    for word in wordList:
        wordMap[word]=True
    if not wordMap.get(endWord,False):
        return ans

    # 创建一个队列，追踪路径
    queue=deque()
    queue.append(beginWord) # 第一个单词入队列



beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
findLadders(beginWord, endWord, wordList)


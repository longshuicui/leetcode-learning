# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/1/30
@function:
79. Word Search (Medium)
https://leetcode.com/problems/word-search/
题目描述
    给定一个字母矩阵，所有的字母都与上下左右四个方向上的字母相连。给定一个字符串，求
    字符串能不能在字母矩阵中寻找到。
输入输出样例
    输入是一个二维字符数组和一个字符串，输出是一个布尔值，表示字符串是否可以被寻找
    到。
    Input: word = "ABCCED",
           board =[["A","B","C","E"],
                   ["S","F","C","S"],
                   ["A","D","E","E"]]
    Output: true
    从左上角的"A" 开始，我们可以先向右、再向下、最后向左，找到连续的"ABCCED"。
题解
    修改访问标记
    对任意位置进行DFS时，首先标记当前位置已访问，避免重复遍历（防止向右搜索又向左返回）；
    当所有的可能都搜索完成后，再回改当前位置为未访问。防止干扰其他位置搜索到当前位置。
    使用回溯法，可以只对一个二维的访问矩阵进行修改，而不用把每次的搜索状态作为一个新对象
    传入到递归函数中
"""


def exist(board, word):
    if len(board) == 0:
        return False
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if backtracking(i, j, 0, board, visited, word):
                return True
    return False


def backtracking(r, c, index, board, visited, word):
    if index==len(word)-1:
        return board[r][c]==word[index]
    if board[r][c]==word[index]:
        visited[r][c]=True
        for nr,nc in ((r+1,c),(r-1,c),(r,c+1),(r,c-1)):
            if 0<=nr<len(board) \
                and 0<=nc<len(board[0]) \
                and not visited[nr][nc] \
                and backtracking(nr,nc,index+1,board,visited,word):
                return True
        visited[r][c]=False

    else:
        return False


board = [["A", "B", "C", "E"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]]
word = "ASFD"
res = exist(board, word)
print(res)

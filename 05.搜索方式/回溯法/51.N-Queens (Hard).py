# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/1/30
@function:
51. N-Queens (Hard)
https://leetcode.com/problems/n-queens/
题目描述
    给定一个大小为 n 的正方形国际象棋棋盘，求有多少种方式可以放置 n 个皇后并使得她们互
    不攻击，即每一行、列、左斜、右斜最多只有一个皇后。
输入输出样例
    输入是一个整数 n，输出是一个二维字符串数组，表示所有的棋盘表示方法。
    Input: 4
    Output: [
                [".Q..", // Solution 1
                "...Q",
                "Q...",
                "..Q."],
                ["..Q.", // Solution 2
                "Q...",
                "...Q",
                ".Q.."]
            ]
    在这个样例中，点代表空白位置， Q 代表皇后。
题解
    和在矩阵中修改字符串类似， 也是通过修改状态矩阵来进行回溯。该题需要对每一行、列、左斜、右斜建立访问数组，
    记录是否存在皇后。
    满足条件的结果中每一行或列有且仅有一个皇后，如果通过对每一行遍历来插入皇后，就不需要对行建立索引数组
"""

import copy


def solveNQueens(n):
    ans = []
    if n == 0:
        return ans
    board = [["." for _ in range(n)] for _ in range(n)]
    column = [False for _ in range(n)]
    ldiag = [False for _ in range(2 * n - 1)]
    rdiag = [False for _ in range(2 * n - 1)]
    backtrack(ans, board, column, ldiag, rdiag, 0, n)
    return [["".join(b) for b in bb] for bb in ans]


def backtrack(ans, board, column, ldiag, rdiag, row, n):
    if row == n:
        ans.append(copy.deepcopy(board))
        return

    for i in range(n):
        if column[i] or ldiag[n - row + i - 1] or rdiag[row + i]:
            continue
        # 修改当前节点状态
        board[row][i] = "Q"
        column[i] = ldiag[n - row + i - 1] = rdiag[row + i] = True
        # 递归子节点
        backtrack(ans, board, column, ldiag, rdiag, row + 1, n)
        # 回改当前子节点
        board[row][i] = "."
        column[i] = ldiag[n - row + i - 1] = rdiag[row + i] = False


n = 4
ans = solveNQueens(n)
print(ans)
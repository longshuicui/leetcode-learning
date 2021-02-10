# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/1/30
@function:
934. Shortest Bridge (Medium)
https://leetcode.com/problems/shortest-bridge/
题目描述
    给定一个二维 0-1 矩阵，其中 1 表示陆地， 0 表示海洋，每个位置与上下左右相连。已知矩
    阵中有且只有两个岛屿，求最少要填海造陆多少个位置才可以将两个岛屿相连。
输入输出样例
    输入是一个二维整数数组，输出是一个非负整数，表示需要填海造陆的位置数。
    Input:
    [[1,1,1,1,1],
    [1,0,0,0,1],
    [1,0,1,0,1],
    [1,0,0,0,1],
    [1,1,1,1,1]]
    Output: 1
题解
    求解两个岛屿的最短距离问题。先用深度优先搜索找到一个岛屿，然后再用广度优先搜索找到最近的岛屿
"""
from collections import deque


def shortestBridgeIteration(grid):
    m, n = len(grid), len(grid[0])

    def neighbors(r, c):
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if 0 <= nr < m and 0 <= nc < n:
                yield nr, nc

    def getIslands():
        # DFS
        done = set()
        islands = []
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val and (i, j) not in done:
                    stack = [(i, j)]  # 入栈
                    seen = {(i, j)}
                    while stack:
                        r, c = stack.pop()  # 出栈
                        for nr, nc in neighbors(r, c):
                            if grid[nr][nc] and (nr, nc) not in seen:  # 判断是否满足条件
                                stack.append((nr, nc))  # 入栈
                                seen.add((nr, nc))
                    done |= seen
                    islands.append(seen)
        return islands

    # 找到岛屿
    source, target = getIslands()
    # BFS
    queue = deque([(node, 0) for node in source])
    done = set(source)
    while queue:
        node, d = queue.popleft()
        if node in target:
            return d - 1
        for nr, nc in neighbors(*node):
            if (nr, nc) not in done:
                queue.append(((nr, nc), d + 1))
                done.add((nr, nc))




grid = [[0, 1, 0],
        [0, 0, 0],
        [0, 0, 1]]
res = shortestBridgeIteration(grid)
print(res)
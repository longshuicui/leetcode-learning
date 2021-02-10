# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/1/28
@function:
695. Max Area of Island (Medium)
题目描述
    给定一个二维的 0-1 矩阵，其中 0 表示海洋， 1 表示陆地。单独的或相邻的陆地可以形成岛
    屿，每个格子只与其上下左右四个格子相邻。求最大的岛屿面积。6.2 深度优先搜索 – 25/143 –
输入输出样例
    输入是一个二维数组，输出是一个整数，表示最大的岛屿面积。
    Input:
    [[0,0,1,0,0,0,0,1,0,0,0,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,1,1,0,1,0,0,0,0,0,0,0,0],
     [0,1,0,0,1,1,0,0,1,0,1,0,0],
     [0,1,0,0,1,1,0,0,1,1,1,0,0],
     [0,0,0,0,0,0,0,0,0,0,1,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    Output: 6
最大的岛屿面积为 6，位于最右侧。

题解
    DFS 深度优先搜索 递归法和迭代法
    每个点都需要遍历上下左右四个方向
"""


def maxAreaOfIslandIteration(grid):
    seen = set()
    ans = 0  # 面积大小
    for r0, row in enumerate(grid):
        for c0, val in enumerate(row):
            if val and (r0, c0) not in seen:
                shape = 0
                stack = [(r0, c0)] # 入栈
                seen.add((r0, c0))
                while stack:
                    r, c = stack.pop() # 出栈
                    shape += 1
                    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):  # 上下左右四个位置
                        if (0 <= nr < len(grid)) and 0 <= nc < len(grid[0]) and grid[nr][nc] and (nr, nc) not in seen:
                            stack.append((nr, nc))
                            seen.add((nr, nc))
                ans = max(ans, shape)

    return ans


def maxAreaOfIslandRecursive(grid):
    seen=set()
    def area(r,c):
        if not (0<=r<len(grid) and 0<=c<len(grid[0]) and (r,c) not in seen and grid[r][c]):
            return 0
        seen.add((r,c))
        return 1+area(r+1,c)+area(r-1,c)+area(r,c-1)+area(r,c+1)
    return max(area(r,c) for r in range(len(grid)) for c in range(len(grid[0])))


grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
# grid = [[0,0,0,0,0]]
ans = maxAreaOfIslandRecursive(grid)
print(ans)

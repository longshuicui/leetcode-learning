# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :  2021/03/24
@function:

给定一个二维坐标中的点的集合，points-list,
points-list=[(x0,y0),(x1,y1),...(xn,yn)]
返回这个列表中斜率为k的两个点

题解：该题是149题的变种题，两个点在同一条直线上，所以说y-kx的值相同，也就是说找到截距相同的两个点
"""

def findPoints(points, k):
    counts={}
    for point in points:
        b=point[1]-k*point[0]
        if b in counts:
            return counts[b], point
        counts[b]=point
    return -1



points=[[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
k=2
res=findPoints(points, k)
print(res)
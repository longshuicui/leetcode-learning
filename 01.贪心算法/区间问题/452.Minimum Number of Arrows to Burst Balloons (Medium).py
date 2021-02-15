# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :  2021/02/15
@function:
452. Minimum Number of Arrows to Burst Balloons (Medium)
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
和435题相似,
区别在于435题求删除的区间，该题求要保留的区间个数。贪心条件该题不取等于的情况
"""

def findMinArrowShots(points):
    if len(points)==0:
        return 0

    points=sorted(points, key=lambda x:x[1],reverse=False)
    print(points)
    total=1
    prev=points[0][1]  # 第一个区间的最后一个坐标
    for i in range(1, len(points)):
        if points[i][0]>prev:
            total+=1
            prev=points[i][1]
    return total



points=[[1,2]]
res=findMinArrowShots(points)
print(res)
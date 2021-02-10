# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/1/26
@function:
605. Can Place Flowers (Easy)
https://leetcode.com/problems/can-place-flowers/
题目描述
    你有一个很长的花坛，其中有些种植了一些，有些没有。然而，鲜花不能种植在  相邻  的地块上。
    给定一个包含0和1的整数数组花坛，其中0表示空，1表示非空，以及一个整数n，返回n个新花是否可以种植在花坛中而不违反无邻接花规则。
输入输出样例
    Input: flowerbed = [1,0,0,0,1], n = 2
    Output: false
"""


def canPlaceFlowers(flowerbed, n):
    size=len(flowerbed)
    hasPlaced=sum(flowerbed)
    if (hasPlaced+n) > size/2:
        return False


flowerbed=[1,0,0,0,0,1]
n=1
res=canPlaceFlowers(flowerbed, n)
print(res)

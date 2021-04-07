# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/4/7
@function:
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
"""


def convert(s, numRows):
    if numRows==1:
        return s
    rows=min(numRows, len(s))
    res=["" for _ in range(rows)]
    curRow, flag=0, -1
    for c in s:
        res[curRow]+=c
        if curRow==0 or curRow==rows-1:
            flag=-flag
        curRow+=flag
    return "".join(res)


s="PAYPALISHIRING"
numRows=1
res=convert(s, numRows)
print(res)
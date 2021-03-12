# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :  2021/03/03
@function:
有若干硬币排成一个序列， 面值依次为[5,1,2,10,6,2],现在规定不能捡相邻的硬币，
请问如何捡硬币才能使捡到的硬币总价值最大

题解：
    创建一个dp数组，第i个硬币捡或不捡，
    如果捡则最大值为 dp[i-2]+nums[i]
    如果不捡，dp[i-1]
    那么dp[i]=max(dp[i-2]+nums[i], dp[i-1])
"""


def coin(nums):
    if len(nums)==0:
        return 0
    dp=[0,nums[0]]
    for i in range(2, len(nums)+1):
        dp.append(max(dp[i-1], dp[i-2]+nums[i-1]))
    return dp[-1]


nums=[5,1,2,10,6,2]
res=coin(nums)
print(res)


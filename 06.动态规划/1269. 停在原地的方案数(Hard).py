# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/5/13
@function:
1269. 停在原地的方案数 (Hard)
https://leetcode-cn.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/
有一个长度为arrLen的数组，开始有一个指针在索引0 处。
每一步操作中，你可以将指针向左或向右移动 1 步，或者停在原地（指针不能被移动到数组范围外）。
给你两个整数steps 和arrLen ，请你计算并返回：在恰好执行steps次操作以后，指针仍然指向索引 0 处的方案数。
由于答案可能会很大，请返回方案数 模10^9 + 7 后的结果。
示例 1：
    输入：steps = 3, arrLen = 2
    输出：4
    解释：3 步后，总共有 4 种不同的方法可以停在索引 0 处。
    向右，向左，不动
    不动，向右，向左
    向右，不动，向左
    不动，不动，不动
示例 2：
    输入：steps = 2, arrLen = 4
    输出：2
    解释：2 步后，总共有 2 种不同的方法可以停在索引 0 处。
    向右，向左
    不动，不动
示例 3：
    输入：steps = 4, arrLen = 2
    输出：8
题解：
    对于计算方案数的题目，常用的方法就是动态规划
    dp[i][j]表示在第i步操作之后，指针位于下标j的方案，0<=i<=steps, 0<=j<=arrLen-1,指针下标不会大于steps,所以0<=j<=min(arrLen-1,steps)
    dp边界，dp[0][0]=1,没有操作且指针位于0的情况，当没有操作指针位于其他下标的情况 dp[0][j]=0 不可能有这种情况
    每一步操作，指针可以向前、向后、不动三种操作，所以得到状态转移方程
    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]+dp[i-1][j+1]
    注意下标越界情况
    最终答案为dp[steps][0]

"""


def numWays(steps, arrLen):
    """时间复杂度O(steps*min(arrLen-1, steps)),
       空间复杂度O(min(arrLen-1, steps))"""
    dp = [0 for _ in range(min(arrLen, steps + 1))]
    dp[0] = 1
    for i in range(1, steps + 1):
        dpNext=[0 for _ in range(min(arrLen, steps + 1))]
        for j in range(min(arrLen, steps + 1)):
            if j == 0:
                dpNext[j] = dp[j] + dp[j + 1]
            elif j == min(arrLen - 1, steps):
                dpNext[j] = dp[j - 1] + dp[j]
            else:
                dpNext[j] = dp[j - 1] + dp[j] + dp[j + 1]
        dp=dpNext
    return dp[0] % (10 ** 9 + 7)


steps = 3
arrLen = 2
res = numWays(steps, arrLen)
print(res)

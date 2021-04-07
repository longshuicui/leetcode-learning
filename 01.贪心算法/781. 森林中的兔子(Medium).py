# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/4/7
@function:
森林中，每个兔子都有颜色。其中一些兔子（可能是全部）告诉你还有多少其他的兔子和自己有相同的颜色。我们将这些回答放在answers数组里。
返回森林中兔子的最少数量。
示例:
    输入: answers = [1, 1, 2]
    输出: 5
    输入: answers = [10, 10, 10]
    输出: 11
题解：
    同一颜色的兔子回答的数量肯定是一样的，但是回答数量相同的，不一定是相同颜色的兔子，所以求最少数量的兔子，就让相同的数的看作
    同一种颜色，贪心思想。不同数量的兔子， 颜色肯定是不一样的，所以：
    将answer中相同的元素分为一组，对于每一组，计算出兔子的最少数量，然后将结果累加，就是最后的结果
    注意如果看到的兔子数量为0， 则说明该颜色只有一只兔子，其他的0只能是不同的颜色

"""


def numRabbits(answers):
    counts={}
    res=0
    for answer in answers:
        counts[answer]=counts.get(answer,0)
        if counts[answer]==0:
            res+=1+answer
            counts[answer]=answer
        else:
            counts[answer]-=1
    return res


answers=[1,0,1,0,0]
ans=numRabbits(answers)
print(ans)
















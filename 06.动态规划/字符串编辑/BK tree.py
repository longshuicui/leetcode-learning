# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/4/25
@function:
实现一个基于编辑距离实现的文本纠错
关键词：编辑距离， BK树， 深度优先搜索， 动态规划

如果输入的词不在字典中，选择编辑距离小于阈值的单词。
暴力思路：query和字典词求编辑距离， 选择最小的K个， 时间复杂度为O(km*max(n))
"""


def calEditDistance(source, target):
    """基于动态规划实现编辑距离 时间复杂度O(mn)
    边界条件：dp[0][j]=j dp[i][0]=i   一个字符串为空时，编辑距离就是第二个字符串的长度
    对于source的i位置和target的j位置
    如果s[i]==t[j]，距离不用变
    如果s[i]!=t[j]，存在替换、插入、删除三种操作
    替换: dp[i-1][j-1]+1
    插入、删除：dp[i][j-1]+1 & dp[i-1][j]+1
    """
    m, n = len(source), len(target)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            else:
                # s[i]等于t[j]
                if source[i - 1] == target[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i - 1][j] + 1, dp[i][j - 1] + 1)

    return dp[m][n]


class TreeNode:
    def __init__(self, word):
        self.word = word
        self.children = {}

    def __str__(self):
        return self.word


class BKTree:
    def __init__(self, words=None):
        self.root = None
        if words:
            for word in words:
                self.add(word)

    def add(self, word):
        if self.root is None:
            self.root = TreeNode(word)
        else:
            node = TreeNode(word)
            curr = self.root
            distance = self._distance(word, curr.word)
            while distance in curr.children:
                curr = curr.children[distance]
                distance = self._distance(word, curr.word)
            curr.children[distance] = node

    def search(self, word, threshold):
        if self.root is None:
            return

        results=[]
        stack=[self.root]
        while len(stack)>0:
            node=stack.pop()
            distance=self._distance(word, node.word)
            if distance<=threshold:
                results.append(node.word)
            # 查询子节点
            for i in range(max(0, distance-threshold), distance+threshold+1):
                next_node=node.children.get(i)
                if next_node:
                    stack.append(next_node)
        return results

    @staticmethod
    def _distance(source, target):
        """求距离"""
        return calEditDistance(source, target)


if __name__ == '__main__':
    words = ["最完美的人生终点", "恐怖爆发", "无名指", "下一站说爱你", "湄公河", "国家地理", "葫芦", "欢乐的朋友们", "名剑"]
    bktree = BKTree(words)
    while True:
        input_token = input("Input: ")
        res = bktree.search(input_token, 2)
        print(res)

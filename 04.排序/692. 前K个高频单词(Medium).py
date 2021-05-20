# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/5/20
@function:
692. 前K个高频单词 (Medium)
https://leetcode-cn.com/problems/top-k-frequent-words/
给一非空的单词列表，返回前 k 个出现次数最多的单词。
返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率，按字母顺序排序。
示例 1：
    输入: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
    输出: ["i", "love"]
    解析: "i" 和 "love" 为出现次数最多的两个单词，均为2次。 注意，按字母顺序 "i" 在 "love" 之前。

示例 2：
    输入: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
    输出: ["the", "is", "sunny", "day"]
    解析: "the", "is", "sunny" 和 "day" 是出现次数最多的四个单词，出现次数依次为 4, 3, 2 和 1 次。

"""
def topKFrequent(words, k):
    freq={}  # 时间复杂度O(n), 空间复杂度O(l)
    for word in words:
        freq[word]=freq.get(word,0)+1

    freq=sorted(freq.items(), key=lambda x:x[0], reverse=False) # 时间复杂度O(nlogn),空间复杂度O(logn)
    freq=sorted(freq, key=lambda x:x[1], reverse=True) # # 时间复杂度O(nlogn),空间复杂度O(logn)

    res=[]
    for i in range(k):
        res.append(freq[i][0])
    return res


words=["i", "love", "leetcode", "i", "love", "coding"]
k=3
res=topKFrequent(words, k)
print(res)
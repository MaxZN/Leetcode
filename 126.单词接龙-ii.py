#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
#

# @lc code=start
def could(a, b):
    assert len(a)==len(b)
    cnt = 0
    for i in range(len(a)):
        if a[i]!=b[i]:
            cnt += 1
    return cnt <= 1

def filter(ret, minlen):
    ans = []
    for item in ret:
        if len(item)==minlen:
            ans.append(item)
    return ans

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList: return []
        ret = []
        self.min_len = float('inf')

        # dfs over time limit.....
        def dfs(cur, tgt, step, waiting = []):
            if step>len(wordList):
                return
            elif could(cur,tgt):
                waiting.append(tgt)
                self.min_len = min(self.min_len, len(waiting))
                ret.append(tuple(waiting))
                waiting.pop()
                return
            else:
                for idx in range(len(wordList)):
                    nex = wordList[idx]
                    if could(cur, nex) and nex not in waiting:
                        waiting.append(nex)
                        dfs(nex, tgt, step+1, waiting)
                        waiting.pop()
        # dfs(beginWord, endWord, 0, [beginWord])
        # ans = filter(ret, self.min_len)

        # 单向BFS
        tree, words, n = collections.defaultdict(set), set(wordList), len(beginWord) 
        if endWord not in wordList: return []
        # found为是否找到最短路径的标识默认False
        # q存储当前层的单词， nq存储下一层的单词
        # tree[x]会记录单词x所有相邻节点的单词，即可能到达最终结果的路径
        found, q, nq = False, {beginWord}, set()
        while q and not found: # 当找到路径或者队列中没有元素时结束
            words -= set(q) # 从words列表中去除当前层的单词，避免重复使用
            for x in q: # 遍历当前层的所有单词
                for y in [x[:i]+c+x[i+1:] for i in range(n) for c in 'qwertyuiopasdfghjklzxcvbnm']: # 改变当前单词的每一个字符
                    if y in words: # 只关心在words集合中的单词
                        if y == endWord: # 如果找到了，将found置为True，不会再继续寻找下一层.
                            found = True
                        else: 
                            nq.add(y) # 准备下一层的单词集合
                        tree[x].add(y) # 记录x单词满足条件的下一个路径
            q, nq = nq, set() # 重新复制q与nq, q为下一次循环需遍历的单词集合,nq置为空
        def bt(x): 
            # 递归，在tree中寻找满足条件的路径
            # for y in tree[x] 遍历当前单词的相邻节点
            return [[x]] if x == endWord else [[x] + rest for y in tree[x] for rest in bt(y)]
        if found == False:
            return []
        return bt(beginWord)

# @lc code=end


#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # dfs，找到与word相匹配的单词
        m, n = len(board), len(board[0])
        w = len(word)

        # i, j为当前坐标，k为当前word匹配到的坐标
        def dfs(i, j, k):
            # 当索引越界，或当前不匹配，或搜索已访问过的坐标时，进行剪枝
            if not 0 <= i < m or not 0 <= j < n or board[i][j] != word[k]: return False
            # 当最后一个字母匹配时，搜索成功
            if k == w - 1: return True
            # 将访问过的字符暂时置为空
            board[i][j] = ''
            # 有上下左右四个搜索方向，搜索下一个字母
            res = dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j-1, k+1) or dfs(i, j+1, k+1)
            # 将访问过的字符还原
            board[i][j] = word[k]
            return res
        
        # 共有MN个起点，每个起点除去回头路有三个搜索方向，故时间复杂度为3**k*MN
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0): return True
        return False


# @lc code=end


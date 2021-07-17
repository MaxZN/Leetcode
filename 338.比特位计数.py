#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]*(n+1)
        if n==0:
            return [0]
        if n==1:
            return [0,1]
        res[0] = 0
        res[1] = 1
        for i in range(2, n + 1):
            if i%2==0:
                res[i] = res[i // 2]
            else:
                res[i] = res[(i-1) // 2] + 1
        return res

        # for i in range(n+1):
        #     bi = set(bin(i))
        #     cnt[i] = bin(i).count('1')
        # return cnt


# @lc code=end


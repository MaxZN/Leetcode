#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        is_primes = [1 for _ in range(2, n)]
        for i in range(2, int(n**0.5)+1):
            if is_primes[i-2]:
                for j in range(i*i, n, i):
                    is_primes[j-2] = 0
        return sum(is_primes)


# @lc code=end


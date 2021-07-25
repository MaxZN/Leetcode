#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res_ = ''
        for i in range(0, len(s), 2*k):
            # 每2k个构建新字符串
            temp = s[i:i+2*k]
            # 判断反转
            if k < len(temp) <= 2*k:
                res = temp[0:k][::-1]+temp[k::]
            else:
                res = temp[::-1]
            res_ += res
        return res_

# @lc code=end


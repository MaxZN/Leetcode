#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        outdic = []
        length = max(len(num1), len(num2)) + 1
        num1_rev = list(num1)[::-1] + ['0'] * (length - len(num1))
        num2_rev = list(num2)[::-1] + ['0'] * (length - len(num2))
        def cal_str(a, b, diff=0):
            input1 = int(a)
            input2 = int(b)
            output = input1 + input2 + diff
            out = str(output % 10)
            diff = output // 10
            return out, diff
        
        diff = 0
        for i in range(length):
            out, diff = cal_str(num1_rev[i], num2_rev[i], diff)
            outdic.append(out)
        if outdic[-1] == '0':
            del outdic[-1]
        return ''.join(outdic[::-1])
        
        

# @lc code=end


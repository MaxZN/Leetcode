#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = ([0] + digits)
        digits.reverse()
        print(digits)
        for i in range(len(digits)):
            raw = digits[i]
            digits[i] += 1
            digits[i] = digits[i] % 10
            if raw != 9:
                break
        digits.reverse()

        if digits[0] == 0:
            return digits[1:]
        else:
            return digits


# @lc code=end


#
# @lc app=leetcode.cn id=507 lang=python3
#
# [507] 完美数
#

# @lc code=start
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num<=1:return False
        dic = [1]
        for i in range(2, int(num**0.5+1)):
            if num % i == 0:
                num1,num2 = i, num//i
                if num1 not in dic: 
                    dic.append(num1)
                if num2 not in dic: 
                    dic.append(num2)
        return num==sum(dic)


# @lc code=end


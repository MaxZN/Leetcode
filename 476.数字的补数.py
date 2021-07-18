#
# @lc app=leetcode.cn id=476 lang=python3
#
# [476] 数字的补数
#

# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        n=bin(num)[2:]#转二进制，从索引2取到最后，因为转二进制后前面会有0b，需要去掉
        c=""
        d=0
        while d<len(n):
            if n[d]=="0":#当n[索引]为"0"，就变成1
                c=c+"1"
            else: 
                c=c+"0"                                                     
            d+=1
        e=int(c,2)#转十进制
        return e

# @lc code=end


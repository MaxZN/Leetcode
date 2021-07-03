#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # method1: forever loop replace 27.37/5.11
        # break_flag = False
        # while len(s)>0 and not break_flag:
        #     len_in = len(s)
        #     s = s.replace('()','')
        #     s = s.replace('[]','')
        #     s = s.replace('{}','')
        #     len_out = len(s)
        #     break_flag = len_in==len_out
        # return len(s)==0

        # method2: stack 70.16/5.11
        Dict = {')':'(', ']':'[', '}':'{'}
        stack = []
        for i in s:
            stack.append(i)
            break_flag = False
            while len(stack)>=2 and not break_flag:
                if stack[-1] in Dict and Dict[stack[-1]]==stack[-2] :
                    stack.pop()
                    stack.pop()
                else:
                    break_flag = True
        return len(stack)==0

        
# @lc code=end


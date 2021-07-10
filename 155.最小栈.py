#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.hash = []

    def push(self, val: int) -> None:
        self.hash.append(val)


    def pop(self) -> None:
        self.hash.pop()


    def top(self) -> int:
        return self.hash[-1]


    def getMin(self) -> int:
        return min(self.hash)



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end


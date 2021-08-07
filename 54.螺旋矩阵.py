#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        self.matrix = matrix
        self.flag = matrix==[]
        if self.matrix==[]: return []
        if type(self.matrix[0])==int: return self.matrix

        out = []
        while not self.flag:
            out += self.get_top()
            print(self.matrix)
            if self.flag: return out
            out += self.get_right()
            print(self.matrix)
            if self.flag: return out
            out += self.get_bot()
            print(self.matrix)
            if self.flag: return out
            out += self.get_left()
            print(self.matrix)
            if self.flag: return out

    def get_top(self):
        top = self.matrix.pop(0)
        self.flag = self.matrix==[]
        return top
    
    def get_bot(self):
        bot = self.matrix.pop(-1)[::-1]
        self.flag = self.matrix==[]
        return bot

    def get_right(self):
        right = []
        for row in range(len(self.matrix)):
            right.append(self.matrix[row].pop(-1))
        self.flag = self.matrix==[]
        if self.matrix[0]==[]:
            self.flag = True
        return right
    
    def get_left(self):
        left = []
        for row in range(len(self.matrix)):
            left.append(self.matrix[row].pop(0))
        self.flag = self.matrix==[]
        if self.matrix[0]==[]:
            self.flag = True
        return left[::-1]
    



# @lc code=end


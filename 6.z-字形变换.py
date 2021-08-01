#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if s=='': return ''
        if len(s)==1: return s
        if numRows==1: return s

        s_id = 0
        extract_id = 0
        lens = len(s)
        stride = 2*numRows - 2
        
        # res = ['' for _ in range(numRows)]
        def get_len_id(s_id, stride, numRows):
            len_id = s_id % stride
            if len_id>=numRows and len_id>=stride:
                return len_id - stride
            elif len_id>=numRows and len_id<stride:
                return stride - len_id
            else:
                return len_id

        res = ['']*numRows
        while s_id < lens:
            len_id = get_len_id(s_id, stride, numRows)
            # print(s_id, stride, numRows, len_id, res)
            res[len_id] += s[s_id]
            s_id += 1
        return ''.join(res)

        '''
        # waste too much time

        import math
        block_len = numRows*2-2
        block_nums = math.ceil(len(s) / block_len)
        mat = [[[''] * numRows \
            for _ in range(numRows-1)] \
            for _ in range(block_nums)]
        
        s_id = 0
        for bn in range(block_nums):
            for row in range(numRows-1):
                for col in range(numRows):
                    # print(bn, row, col, mat[bn][row])
                    if row==0 and s_id<len(s):
                        mat[bn][row][col] = s[s_id]
                        s_id += 1
                    elif (col+row+1) % numRows==0 and s_id<len(s):
                        mat[bn][row][col] = s[s_id]
                        s_id += 1
                    else:
                        pass

        sout = ''
        for col in range(numRows):
            for bn in range(block_nums):
                for row in range(numRows-1):
                    sout += mat[bn][row][col]
        return sout
        '''


# @lc code=end


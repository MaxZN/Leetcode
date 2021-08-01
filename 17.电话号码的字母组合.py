#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        phone = {'2':['a','b','c'],
                 '3':['d','e','f'],
                 '4':['g','h','i'],
                 '5':['j','k','l'],
                 '6':['m','n','o'],
                 '7':['p','q','r','s'],
                 '8':['t','u','v'],
                 '9':['w','x','y','z']}
        layers = []
        for d in digits:
            layers.append(phone[d])
        num_layers = len(layers)
        print(num_layers)

        res = []
        ans = []
        def dfs(cnt_layers):
            if cnt_layers==num_layers:
                res.append(''.join(ans))
            else:
                for s in layers[cnt_layers]:
                    ans.append(s)
                    dfs(cnt_layers+1)
                    ans.pop()
        dfs(0)
        return res


# @lc code=end


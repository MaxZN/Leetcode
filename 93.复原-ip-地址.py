#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原 IP 地址
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def dfs(templist, start_id):
            if start_id==len(s) and len(templist)==4:
                ans.append('.'.join(templist))
                return
            elif start_id==len(s) or len(templist)==4:
                return
            elif s[start_id]=='0':
                dfs(templist+['0'], start_id+1)
            else:
                wait_val = 0
                for idx in range(start_id, len(s)):
                    wait_val = wait_val*10 + int(s[idx])
                    if wait_val<=255:
                        dfs(templist+[str(wait_val)],idx + 1)
                    else:
                        break
        dfs([],0)
        return ans


# @lc code=end


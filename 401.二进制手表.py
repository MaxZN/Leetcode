#
# @lc app=leetcode.cn id=401 lang=python3
#
# [401] 二进制手表
#

# @lc code=start
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans_all=[]
        # 首先找到二进制中1的数目为turnedOn的所有数字
        # hours=[0,0,0,0] minuts=[0,0,0,0,0,0]
        for k_hour in range(0,min(4,turnedOn)+1):
            k_minuts=turnedOn-k_hour
            H, M=self.comb(4, k_hour),self.comb(6,k_minuts)
            for h in H:
                for m in M:
                    hs, ms=self.get_hours(h),self.get_minutes(m)
                    if hs!='' and ms!='':
                        ans_all.append(hs+':'+ms)
        return ans_all
    # 从[0,...,n-1]里面选择k个数字 1<=k<=n
    # 一共n个灯 k个亮灯 k>=1返回所有可能组合
    def comb(self, n, k):
        ans_all=[]
        def dfs(candidates, ans):
            if len(ans)==k: ans_all.append(ans)
            for i in range(len(candidates)):
                dfs(candidates[i+1:], ans+[candidates[i]])
        dfs(list(range(n)),[])
        return ans_all
    # 由小时亮灯列表计算小时字符串           
    def get_hours(self, l):
        hours_list, hours=[1,2,4,8],0
        for k in l:
            hours+=hours_list[k]
        if 0<=hours<12: return str(hours)
        return ''
    # 由分钟亮灯列表计算分钟字符串        
    def get_minutes(self, l):
        minutes_list, minutes=[1,2,4,8,16,32],0
        for k in l:
            minutes+=minutes_list[k]
        if minutes>59: return ''
        m=str(minutes) if minutes>=10 else '0'+str(minutes)
        return m 

# @lc code=end


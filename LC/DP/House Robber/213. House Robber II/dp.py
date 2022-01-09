class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        def dfs(lst):
            N=len(lst)
            dp=[[0]*2 for i in range(N)]
            #0 not rob
            #1 rob
            dp[0][1]=lst[0]
            
            for i in range(1,N):
                dp[i][0]=max(dp[i-1][0],dp[i-1][1])
                dp[i][1]=max(dp[i-1][1],dp[i-1][0]+lst[i])
            return max(dp[-1][0],dp[-1][1])
        
        return max(dfs(nums[:-1]),dfs(nums[1:]))

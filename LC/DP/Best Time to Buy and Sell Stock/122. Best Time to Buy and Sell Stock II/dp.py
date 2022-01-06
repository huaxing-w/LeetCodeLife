class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N=len(prices)
        ans=0
        dp=[[0]*2 for i in range(N)]
        dp[0][0]=0
        dp[0][1]=-prices[0]
        for i in range(1,N):
            dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i])
            dp[i][1]=max(dp[i-1][1],dp[i-1][0]-prices[i])
            ans=max(dp[i][0],dp[i][1])
        print(dp)
        return ans
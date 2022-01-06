class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        N=len(prices)
        #0 buy
        #1 sell
        dp=[[0]*2 for i in range(N)]
        dp[0][0]=-prices[0]

        for i in range(1,N):
            dp[i][0]=max(dp[i-1][0],dp[i-1][1]-prices[i])
            dp[i][1]=max(dp[i-1][1],dp[i-1][0]+prices[i]-fee)
        return dp[-1][1]
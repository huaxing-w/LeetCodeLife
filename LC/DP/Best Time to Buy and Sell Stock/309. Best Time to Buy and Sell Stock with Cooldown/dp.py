class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N=len(prices)
        if N==1:
            return 0
        dp=[[0]*3 for i in range(N)]
        #0 in cool down
        #1 buy stock
        #2 sell stock

        dp[0][0]=0
        dp[0][1]=-prices[0]
        dp[1][2]=0

        ans=0
        for i in range(1,N):
            dp[i][0]=max(dp[i-1][0],dp[i-1][2])
            dp[i][1]=max(dp[i-1][1],dp[i-1][0]-prices[i])
            dp[i][2]=max(dp[i-1][2],dp[i-1][1]+prices[i])
             
        print(dp)
        return dp[-1][2]
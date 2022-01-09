class Solution:
    def numTrees(self, n: int) -> int:
        if n==1:
            return 1
        dp=[1]*(n+1)
        dp[1]=1
        dp[2]=2

        for i in range(3,n+1):
            temp=[j for j in range(1,i+1)]
            cur=0
            N=len(temp)
            for k in range(N):
                a=dp[k-0]
                b=dp[N-1-k]
                cur+=a*b
            dp[i]=cur
        return dp[-1]

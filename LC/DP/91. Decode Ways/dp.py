class Solution:
    def numDecodings(self, s: str) -> int:
        temp=[str(i) for i in range(1,27)]
        N=len(s)
        s='#'+s
        
        dp=[0]*(N+1)
        dp[0]=1
        for i in range(1,N+1):
            if s[i]!='0':
                dp[i]+=dp[i-1]
            if i>1 and s[i-1:i+1] in temp:
                dp[i]+=dp[i-2]
        print(dp)
        return dp[-1]

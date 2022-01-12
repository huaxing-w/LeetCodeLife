class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m=len(s1)
        n=len(s2)

        s1='#'+s1
        s2='#'+s2

        dp=[[math.inf]*(n+1) for _ in range(m+1)]

        dp[0][0]=0
        for i in range(1,m+1):
            dp[i][0]=dp[i-1][0]+ord(s1[i])
        for j in range(1,n+1):
            dp[0][j]=dp[0][j-1]+ord(s2[j])


        for i in range(1,m+1):
            for j in range(1,n+1):
                if s1[i]==s2[j]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j]+ord(s1[i]),dp[i][j-1]+ord(s2[j]))
        return dp[m][n]

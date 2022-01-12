class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m=len(s1)
        n=len(s2)
        l=len(s3)
        if m+n!=l:
            return False
        s1='#'+s1
        s2='#'+s2
        s3='#'+s3
        dp=[[False]*(n+1) for i in range(m+1)]

        dp[0][0]=True

        for j in range(1,n+1):
            if dp[0][j-1] and s2[j]==s3[j]:
                dp[0][j]=True
        for i in range(1,m+1):
            if dp[i-1][0] and s1[i]==s3[i]:
                dp[i][0]=True

        for i in range(1,m+1):
            for j in range(1,n+1):
                if s1[i]==s3[i+j] and dp[i-1][j]:
                    dp[i][j]=True
                elif  s2[j]==s3[i+j] and dp[i][j-1]:
                    dp[i][j]=True
        return dp[m][n]

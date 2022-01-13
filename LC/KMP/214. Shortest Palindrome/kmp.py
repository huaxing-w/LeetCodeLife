class Solution:
    def shortestPalindrome(self, t: str) -> str:
        if t=='':
            return ''

        def findSuffix(s):
            N=len(s)
            dp=[0]*N
            for i in range(1,N):
                j=dp[i-1]
                while j>=1 and s[i]!=s[j]:
                    j=dp[j-1]
                if s[i]==s[j]:
                    dp[i]=j+1
            return dp
        

        p=t
        s=p[::-1]

        suffix=findSuffix(p)
        N=len(s)

        dp=[0]*N
        if p[0]==s[0]:
            dp[0]=1
        for i in range(1,N):
            j=dp[i-1]
            while j>0 and s[i]!=p[j]:
                j=suffix[j-1]
            if s[i]==p[j]:
                dp[i]=j+1
        
        len_=dp[N-1]
        B=p[len_:][::-1]
        return B+p

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m=len(haystack)
        n=len(needle)
        if m==0:
            return 0
        if n==0:
            return -1

        def findsufix(s):
            N=len(s)
            dp=[0]*N
            for i in range(1,N):
                j=dp[i-1]
                while j>=1 and s[i]!=s[j]:
                    j=dp[j-1]
                if s[i]==s[j]:
                    dp[i]=j+1
            return dp 
        
        suffix=findsufix(needle)

        N=len(haystack)
        dp=[0]*N
        for i in range(1,N):
            j=dp[i-1]
            while j>0 and haystack[i]!=needle[j]:
                j=suffix[j-1]
            if haystack[i]==needle[j]:
                dp[i]=j+1
            
            if dp[i]==len(needle):
                return i-len(needle)+1
        return -1

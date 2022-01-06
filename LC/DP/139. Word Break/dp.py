class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N=len(s)
        dp=[False]*(N+1)
        dp[0]=True
        for i in range(N):
            for j in range(i+1,N+1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j]=True
        return dp[-1]
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N=len(s)
        @lru_cache(None)
        def dfs(i):
            if i>=N:
                return True
            for j in range(1,20):
                if s[i:i+j] in wordDict and dfs(i+j):
                    print(s[i:i+j])
                    return True
            return False
        
        return dfs(0)
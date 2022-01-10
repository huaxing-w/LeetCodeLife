class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def check(lst):

            N=len(lst)
            if N<3:
                return False
            for i in range(N-2):
                if lst[i]+lst[i+1]==lst[i+2]:
                    continue
                else:
                    return False
            return True
        
        N=len(num)
        def dfs(s,cur):
            if not s:
                if check(cur):
                    print(s,cur)
                    return True
                return False
            
            N=len(s)
            for j in range(N):
                if s[:j+1][0]=='0' and len(s[:j+1])>1:
                    continue
                else:
                    if dfs(s[j+1:],cur+[int(s[:j+1])]):
                        return True 
            return False
        
        return dfs(num,[])

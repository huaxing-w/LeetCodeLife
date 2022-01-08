class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        N=len(candidates)

        def dfs(i,path,rest):
            if rest==0:
                ans.append(path[:])
                return 
            for j in range(i,N):
                if candidates[j]>rest:
                    break
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                path.append(candidates[j])
                dfs(j+1,path,rest-candidates[j])
                path.pop()
        candidates.sort()
        dfs(0,[],target)
        return ans

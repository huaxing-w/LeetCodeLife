class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        N=len(nums)
        visited=[False]*N
        temp=[]
        def dfs(i):
            if i==N:
                ans.append(nums[:])
                return 
            
            for j in range(0,N):
                if visited[j] or (j>0 and nums[j]==nums[j-1] and not visited[j-1]):
                    continue
                temp.append(nums[j])
                visited[j]=True 
                dfs(i+1)
                visited[j]=False
                temp.pop()
        dfs(0)
        return ans

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix=[0]
        for i in nums:
            prefix.append(prefix[-1]+i)
        N=len(nums)
        ans=N+1
        stack=[]
        q=collections.deque()
        for i,value in enumerate(prefix):
            while q and value <=prefix[q[-1]]:
                q.pop()
            while q and value-prefix[q[0]]>=k:
                index=q.popleft()
                ans=min(ans,i-index)
            q.append(i)
        return ans if ans<N+1 else -1 

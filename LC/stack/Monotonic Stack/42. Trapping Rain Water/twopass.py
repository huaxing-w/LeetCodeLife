class Solution:
    def trap(self, height: List[int]) -> int:
        N=len(height)
        left_high=[0]*N
        cur_max=0
        for i,value in enumerate(height):
            left_high[i]=cur_max
            cur_max=max(cur_max,value)
        
        right_high=[0]*N
        cur_max=0
        for i in range(N-1,-1,-1):
            right_high[i]=cur_max
            cur_max=max(cur_max,height[i])
        
        print(left_high)
        print(height)
        print(right_high)
        
        ans=0
        for i in range(N):
            if left_high[i]>=height[i]<=right_high[i]:
                ans+=min(left_high[i],right_high[i])-height[i]
        return ans 

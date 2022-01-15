class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        N=len(nums)
        prevSmall=[]
        cur=nums[0]
        for i in nums:
            prevSmall.append(cur)
            cur=min(cur,i)

        prevBig=[-1]*N
        stack=[]
        for i in range(N-1,-1,-1):
            if not stack or stack[-1][0]>=nums[i]:
                stack.append((nums[i],i))
            else:
                while stack and stack[-1][0]<nums[i]:
                    value,index=stack.pop()
                    prevBig[index]=i
                stack.append((nums[i],i))
        print(prevSmall)
        print(prevBig)

        for i in range(N-1,-1,-1):
            pBigIndex=prevBig[i]
            if 1<=pBigIndex<=N-2:
                if nums[pBigIndex]>prevSmall[pBigIndex] and prevSmall[pBigIndex]<nums[i]:
                    return True
        return False

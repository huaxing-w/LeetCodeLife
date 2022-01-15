class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N=len(heights)
        nextSmaller=[N-1]*N
        stack=[]
        for i,value in enumerate(heights):
            if not stack or stack[-1][0]<=value:
                stack.append((value,i))
            else:
                while stack and stack[-1][0]>value:
                    num,index=stack.pop()
                    nextSmaller[index]=i-1
                stack.append((value,i))
        print(nextSmaller)

        prevSmaller=[0]*N
        stack=[]
        for i in range(N-1,-1,-1):
            if not stack or stack[-1][0]<=heights[i]:
                stack.append((heights[i],i))
            else:
                while stack and stack[-1][0]>heights[i]:
                    num,index=stack.pop()
                    prevSmaller[index]=i+1
                stack.append((heights[i],i))
        print(prevSmaller)
        ans=0
        for i in range(N):
            left=prevSmaller[i]
            right=nextSmaller[i]
            ans=max(ans,(right-left+1)*heights[i])
        return ans 

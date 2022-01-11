class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        N=len(growTime)
        temp=[]
        for i,j in zip(plantTime,growTime):
            temp.append((i+j,i,j))
        temp.sort(key=lambda x:-x[2])
        print(temp)
        ans=0
        cur=0
        for i in temp:
            ans=max(ans,cur+i[0])
            cur+=i[1]
        return ans 

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        l=1
        r=10**10
        N=len(growTime)
        def check(t):
            temp=[]
            for i in range(N):
                temp.append((plantTime[i],t-growTime[i]))
            temp.sort(key=lambda x:x[1])
            cur=0
            for i in range(N):
                cur+=temp[i][0]
                if cur>temp[i][1]:
                    return False
            return True 

        while l<r:
            mid=(l+r)//2
            if check(mid):
                r=mid
            else:
                l=mid+1
        return l

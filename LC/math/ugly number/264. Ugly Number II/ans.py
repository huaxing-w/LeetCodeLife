class Solution:
    def nthUglyNumber(self, n: int) -> int:
        h=[1]
        
        count=1
        seen=set()
        while count!=n:
            # print(h)
            pop=heapq.heappop(h)
            for i in [2,3,5]:
                if i*pop not in seen:
                    heapq.heappush(h,i*pop)
                    seen.add(i*pop)
            count+=1
        return h[0]

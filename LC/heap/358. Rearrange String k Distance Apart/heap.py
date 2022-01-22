class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        N=len(s)
        if k==0:
            return s
        dic=collections.Counter(s)
        h=[]
        q=collections.deque()
        max_=max(dic.values())
        print(max_)
        
        for i in dic:
            heapq.heappush(h,(-dic[i],i))
        ans=''
        while h:
            left,letter=heapq.heappop(h)
            ans+=letter
            q.append((-left-1,letter))
            if len(q)==k:
                left_q,left_letter=q.popleft()
                if left_q>0:
                    heapq.heappush(h,(-left_q,left_letter))
            
        if len(ans)<N:
            return ''
        return ans 

class Solution:
    def longestDupSubstring(self, s: str) -> str:
        # create two power base
        p1=random.randint(26,100)
        p2=random.randint(26,100)

        #create two mod
        m1=random.randint(10**9+7,2**31-1)
        m2=random.randint(10**9+7,2**31-1)

        N=len(s)
        
        count=1
        dic={}
        for i in range(97,123):
            dic[chr(i)]=count
            count+=1
        
        l=1
        r=N

        def check(mid):
            offset1=pow(p1,mid,m1)
            offset2=pow(p2,mid,m2)
            cur1=0
            cur2=0
            for i in range(mid):
                cur1=(cur1*p1+dic[s[i]])%m1
                cur2=(cur2*p2+dic[s[i]])%m2
            seen={(cur1,cur2)}
            

            for i in range(mid,N):
                cur1=(cur1*p1+dic[s[i]]-dic[s[i-mid]]*offset1)%m1
                cur2=(cur2*p2+dic[s[i]]-dic[s[i-mid]]*offset2)%m2
                
                if (cur1,cur2) in seen:
                    return i-mid+1
                seen.add((cur1,cur2))
            return -1
        

        start=-1
        len_=1
        while l<=r:
            mid=(l+r+1)//2
            index= check(mid)
            if index!=-1:
                l=mid+1
                start=index
                len_=mid
            else:
                r=mid-1
        return s[start:start+len_]

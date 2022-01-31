class Solution:
    def longestPrefix(self, s: str) -> str:
        N=len(s)
        prefix=0
        sufix=0
        dic={}
        count=1
        for i in range(97,123):
            dic[chr(i)]=count
            count+=1
        ans=0
        p=31
        mul=1
        mod=10**9+7
        for i in range(N-1):
            
            prefix=(prefix*p+dic[s[i]])%mod
            sufix=(sufix+dic[s[N-i-1]]*mul)%mod
            
            if prefix==sufix:
                ans=i+1
            mul=mul*p%mod
        return s[:ans]

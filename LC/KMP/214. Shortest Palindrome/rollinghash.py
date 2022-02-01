class Solution:
    def shortestPalindrome(self, s: str) -> str:
        N=len(s)
        if s==s[::-1]:
            return s
        ans=-1
        dic={}
        count=1
        for i in range(97,123):
            dic[chr(i)]=count
            count+=1
        
        p=31
        mod=10**9+7
        mul=1
        
        l=0
        r=0
        for i in range(N):
            l=(l*p+dic[s[i]])%mod
            r=(r+dic[s[i]]*mul)%mod
            mul=mul*p%mod

            if l==r:
                ans=i
        
        if ans==N-1:
            return s[::-1]+s
        else:
            return s[ans+1:][::-1]+s

class Solution:
    def longestDecomposition(self, text: str) -> int:
        N=len(text)
        l=0
        r=N-1
        ans=0
        
        cur_l=0
        cur_r=0
        p=31
        mul=1
        mod=10**9+7

        count=1
        dic={}
        for i in range(97,123):
            dic[chr(i)]=count
            count+=1

        while l<r:
            cur_l=(cur_l*p+dic[text[l]])%mod
            cur_r=(cur_r+dic[text[r]]*mul)%mod

            if cur_l==cur_r:
                ans+=2
                if l+1==r:
                    return ans
                cur_l=0
                cur_r=0
                mul=1

            else:
                mul=mul*p
            l+=1
            r-=1
        return ans+1 

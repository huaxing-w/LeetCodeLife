class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        N=len(text)
        dic={}
        count=1
        for i in range(97,123):
            dic[chr(i)]=count
            count+=1
        
        p=31
        mod=10**9+7
        ans=set()
        for k in range(1,N):
            dic1={}
            offset=pow(p,k,mod)
            cur=0
            for i in range(N):
                cur=(cur*p+dic[text[i]])%mod
                if i-k>=0:
                    cur=(cur-dic[text[i-k]]*offset)%mod
                    if i-k in dic1 and dic1[i-k]==cur:
                        ans.add(text[i-k+1:i+1])
                if i+1>=k:
                    dic1[i]=cur
                    
        return len(ans)

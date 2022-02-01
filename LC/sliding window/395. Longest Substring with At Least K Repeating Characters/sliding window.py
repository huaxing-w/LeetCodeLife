class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        N=len(s)
        ans=0
        for i in range(1,26):
            dic={}
            unique=0
            l=0
            for j in range(N):
                if s[j] in dic:
                    dic[s[j]]+=1
                else:
                    dic[s[j]]=1
                
                if dic[s[j]]==1:
                    unique+=1
                while unique>i:
                    dic[s[l]]-=1
                    if dic[s[l]]==0:
                        dic.pop(s[l])
                        unique-=1
                    l+=1
                if unique==i:
                    for item in dic:
                        if dic[item]<k:
                            break
                    else:
                        ans=max(ans,j-l+1)
        return ans

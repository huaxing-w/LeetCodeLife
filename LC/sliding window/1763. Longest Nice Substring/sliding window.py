class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        N=len(s)
        max_=0
        ans=''
        for i in range(1,26):
            dic={}
            unique=0
            l=0
            for j in range(N):
                letter=s[j]
                if letter.lower() in dic or letter.upper() in dic:
                    if letter not in dic:
                        dic[letter]=1
                    else:
                        dic[letter]+=1
                else:
                    dic[letter]=1
                    unique+=1
                
                
                while unique>i:
                    left=s[l]
                    dic[left]-=1
                    if dic[left]==0:
                        dic.pop(left)
                    if left.lower() not in dic and left.upper() not in dic:
                        unique-=1
                    l+=1
                
                if unique==i:
                    for item in dic:
                        temp=item.lower()
                        temp1=item.upper()
                        if temp not in dic or temp1 not in dic:
                            break
                    else:
                        if j-l+1>max_:
                            max_=j-l+1
                            ans=s[l:j+1]
        return ans 

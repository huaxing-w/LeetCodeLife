class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num)<=k:
            return '0'
        stack=[]
        count=0
        for i in num:
            cur=int(i)
            if not stack or stack[-1]<=cur or count==k:
                stack.append(cur)
            else:
                while stack and stack[-1]>cur and count<k:
                    stack.pop()
                    count+=1
                stack.append(cur)
        while count!=k:
            stack.pop()
            count+=1
        
        return str(int(''.join([str(i) for i in stack])))

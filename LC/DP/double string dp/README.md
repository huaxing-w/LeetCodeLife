# template

okay, so here is the temple

it is very powerful

remember it by heart

```python

#find the length of s1,s2

m=len(s1)
n=len(s2)

#make s1,s2 1 index

s1='#'+s1
s2='#'+s2

#create dp array, here length is m+1 and n+1

dp=[[False]*(n+1) for _ in range(m+1)]

#write the main part first and then come back for the edge case!!!

#here they are all from 1 to len+1
for i in range(1,m+1):
    for j in range(1,n+1):
        #typical transformation formula 
        '''
        dp[i][j]~{
            dp[i-1][j-1]
            dp[i-1][j]
            dp[i][j-1]
        this varys by different problem
        }
        '''

# okay, how to find the edge case?
#based on your dp formula, which part we have not covered?
#since we start from 1 index
#if there is a case where we need to use dp[0][j] or dp[i][0]
#here we need to cover the case 

'''
for i in range(m):
    dp[i][0]...

for j in range(n):
    dp[0][j]...
'''

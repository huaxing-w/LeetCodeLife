# reflection 2022-01-05
the top down solution is trivial
<br/>
Just remember to do the memorization 
<br/>
<br/>
the tircky part in the dp solution
```python
for i in range(N):
    for j in range(i+1,N+1):
        if dp[i] and s[i:j] in wordDict:
            dp[j]=True
```
remember dp array has actually 1 length longer than the actual string
<br/>
so dp[i] represent the the word end in index i-1
<br/>
or you could say, the s[i] is the next word after dp array


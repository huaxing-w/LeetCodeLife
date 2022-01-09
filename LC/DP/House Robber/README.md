2022-01-09
okay, question

for the rob day

should we do
```python
dp[i][1]=max(dp[i-1][1],dp[i-1][0]+lst[i])
```
or we should do 

```python
dp[i][1]=dp[i-1][0]+lst[i]
```

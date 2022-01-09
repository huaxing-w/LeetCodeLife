you should be comfortable with 

look at the exit condition


```python
def dfs(i,j,index):
    if index==N-1:
        return True 
    visited[i][j]=True
    for dx,dy in dir:
        nx=i+dx
        ny=j+dy
        if 0<=nx<m and 0<=ny<n and not visited[nx][ny]:
            if board[nx][ny]==word[index+1] and dfs(nx,ny,index+1):
                return True 
    visited[i][j]=False
    return False

```

here index can only get to N-1, but not N as usually

why is that??

```python
if board[nx][ny]==word[index+1] and dfs(nx,ny,index+1):
```

here we already checked, if the next word is the same then we can process to the next round, so the last one would be N-1

BE FLEXIBLE

```python
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        g=collections.defaultdict(list)
        for i,j in dislikes:
            g[i].append(j)
            g[j].append(i)
        dic={}
        def dfs(node,c=0):
            if node in dic:
                return dic[node]==c
            dic[node]=c
            for nxt in g[node]:
                if not dfs(nxt,c^1):
                    return False
            return True
        
        for i in range(1,n+1):
            if i not in dic:
                if not dfs(i):
                    return False
        return True
```

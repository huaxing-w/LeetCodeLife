```python
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        N=len(graph)

        dic={}
        def dfs(node, c=0):
            if node in dic:
                return dic[node]==c
            dic[node]=c

            for nxt in graph[node]:
                if not dfs(nxt,c^1):
                    return False
            return True  
        
        for i in range(N):
            if i not in dic:
                if not dfs(i):
                    return False
        return True 

```

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        
        dic=collections.defaultdict(list)
        for i,j in edges:
            dic[i].append(j)
            dic[j].append(i)
        visited=[False]*n
        def dfs(i):
            if visited[i]:
                return 
            visited[i]=True
            for nxt in dic[i]:
                dfs(nxt)
        dfs(0)
        print(visited)
        for i in visited:
            if i==False:
                return False
        return True

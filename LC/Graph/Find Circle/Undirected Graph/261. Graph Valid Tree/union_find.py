class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent=[i for i in range(n)]
        def u_find(x):
            if parent[x]!=x:
                parent[x]=u_find(parent[x])
            return parent[x]
        def u_union(x,y):
            temp1=u_find(x)
            temp2=u_find(y)
            if temp1!=temp2:
                parent[temp1]=temp2
                return True 
            else:
                return False
        
        for i,j in edges:
            if not u_union(i,j):
                return False
        count=0
        for i in range(n):
            if i==parent[i]:
                count+=1
                if count>1:
                    return False
        return True 

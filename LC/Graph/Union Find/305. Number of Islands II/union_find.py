class UF:
    def __init__(self,N):
        self.parent=[i for i in range(N)]
        self.rank=[1]*N
        self.size=0
    
    def u_find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.u_find(self.parent[x])
        return self.parent[x]
    
    def u_union(self,x,y):
        temp1=self.u_find(x)
        temp2=self.u_find(y)
        if temp1!=temp2:
            if self.rank[temp1]<self.rank[temp2]:
                self.parent[temp1]=temp2
            else:
                self.parent[temp2]=temp1
                if self.rank[temp1]==self.rank[temp2]:
                    self.rank[temp1]+=1
            self.size-=1

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf=UF(m*n)
        mat=[[0]*n for _ in range(m)]
        print(mat)
        dir=[(0,1),(0,-1),(1,0),(-1,0)]
        seen=set()
        ans=[]
        for i,j in positions:
            
            id=i*n+j
            print(id)
            if id in seen:
                mat[i][j]=1
                ans.append(uf.size)
                continue
            seen.add(id)
            uf.size+=1
            for dx,dy in dir:
                nx=i+dx
                ny=j+dy
                if 0<=nx<m and 0<=ny<n and mat[nx][ny]==1:
                    id2=nx*n+ny
                    uf.u_union(id,id2)
            mat[i][j]=1
            ans.append(uf.size)
        print(mat)
        return ans 

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])
        N=len(word)
        dir=[(0,1),(0,-1),(1,0),(-1,0)]
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

        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    visited=[[False]*n for _ in range(m)]
                    if dfs(i,j,0):
                        return True 
        return False

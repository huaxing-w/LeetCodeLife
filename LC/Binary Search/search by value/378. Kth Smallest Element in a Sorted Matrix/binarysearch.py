class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n=len(matrix)
        l=-10**9
        r=10**9

        def check(mid):
            i=n-1
            j=0
            count=0

            while i>=0 and j<n:
                if matrix[i][j]<=mid:
                    count+=i+1
                    j+=1
                else:
                    i-=1
            return count

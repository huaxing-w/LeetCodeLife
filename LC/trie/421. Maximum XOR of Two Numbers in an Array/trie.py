class Trie:
    def __init__(self):
        # point to 0
        self.left=None
        # point to 1
        self.right=None

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root=Trie()

        def add(num):
            cur=root
            for k in range(30,-1,-1):
                bit=(num>>k)&1
                if bit==0:
                    if not cur.left:
                        cur.left=Trie()
                    cur=cur.left
                else:
                    if not cur.right:
                        cur.right=Trie()
                    cur=cur.right
        
        def check(num):
            cur=root
            x=0
            for k in range(30,-1,-1):
                bit=(num>>k)&1
                if bit==0:
                    if cur.right:
                        cur=cur.right
                        x=(x<<1)+1
                    else:
                        cur=cur.left
                        x=(x<<1)
                else:
                    if cur.left:
                        cur=cur.left
                        x=(x<<1)+1
                    else:
                        cur=cur.right
                        x=x<<1
            return x

        ans=0
        N=len(nums)
        for i in range(1,N):
            add(nums[i-1])
            ans=max(ans,check(nums[i]))
        return ans 

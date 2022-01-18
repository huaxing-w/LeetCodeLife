```python
class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, nums: List[int]) -> int:
        
        root = TreeNode(nums[0] % 10)               
        for num in nums[1: ]:                       
            depth, pos, val = num//100, (num//10)%10, num%10
            pos -= 1                                
            p = root                                
            for d in range(depth - 2, -1, -1):
                if pos < (1<<d):                    #p's left node
                    if p.left:
                        p = p.left
                    else:
                        p.left = TreeNode(val)      
                else:
                    if p.right:
                        p = p.right
                    else:
                        p.right = TreeNode(val)
                pos %= (1 << d)                     #here is the most important part and very hard to understand

        self.res = 0
        self.dfs(root, 0)
        return self.res

    def dfs(self, rt: TreeNode, cur_sum: int) -> None:  
        if rt == None:
            return 
        cur_sum += rt.val
        if rt.left==None and rt.right==None:            
            self.res += cur_sum
            return 
        if rt.left:                                     
            self.dfs(rt.left, cur_sum)
        if rt.right:
            self.dfs(rt.right, cur_sum)



```


> pos %= (1 << d)   


this part is super hard

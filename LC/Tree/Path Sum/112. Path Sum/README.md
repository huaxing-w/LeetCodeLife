```python
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        def dfs(node,cur):
            if not node.left and not node.right:
                cur+=node.val
                if cur==targetSum:
                    return True
                return False
            
            cur+=node.val
            l=node.left is not None and dfs(node.left,cur)
            r=node.right is not None and dfs(node.right,cur)
            
            return l or r

        return dfs(root,0)

```

nothing to talk about 


but it is true false recursive pattern
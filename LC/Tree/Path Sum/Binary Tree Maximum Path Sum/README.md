```python
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans=-10**10
        def dfs(node):
            nonlocal ans 
            if not node:
                return 0
            l=max(0,dfs(node.left))
            r=max(0,dfs(node.right))
            ans=max(ans,node.val+l+r)
            return node.val+max(l,r)
        dfs(root)
        return ans 

```

typ recursion function itself is not used to find the ans, but we update the ans along with the recursion

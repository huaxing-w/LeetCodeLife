```python
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans=[]
        if not root:
            return ans
        def dfs(node,cur,temp):
            if not node.left and not node.right:
                if cur+node.val==targetSum:
                    ans.append(temp+[node.val])
                return 
            
            if node.left:
                dfs(node.left,cur+node.val,temp+[node.val])
            if node.right:
                dfs(node.right,cur+node.val,temp+[node.val])
        dfs(root,0,[])
        return ans 
```


bring temp+[node.val] to the next recursion

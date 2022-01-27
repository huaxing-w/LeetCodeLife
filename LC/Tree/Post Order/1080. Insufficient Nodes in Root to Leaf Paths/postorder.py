class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        def dfs(node,cur,limit):
            if node.left is None and node.right is None:
                return cur+node.val<limit
            l=True
            r=True
            if node.left:
                l=dfs(node.left,cur+node.val,limit)
            if node.right:
                r=dfs(node.right,cur+node.val,limit)
            
            if l:
                node.left=None
            if r:
                node.right=None
            
            return l and r
        
        if dfs(root,0,limit):
            return None
        return root

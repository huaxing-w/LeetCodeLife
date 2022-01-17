class Solution:
    def rob(self, root: TreeNode) -> int:
        
        dic={}
        def dfs(node,rob):
            if (node,rob) in dic:
                return dic[(node,rob)]
            if not node:
                return 0
            if rob==0:
                best=max(dfs(node.left,1),dfs(node.left,0))+max(dfs(node.right,1),dfs(node.right,0))
                dic[(node,rob)]=best
                return best
            if rob==1:
                best=node.val+dfs(node.left,0)+dfs(node.right,0)
                dic[(node,rob)]=best
                return best
        
        return max(dfs(root,0),dfs(root,1))

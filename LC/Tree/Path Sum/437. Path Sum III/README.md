```python
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        dic=collections.Counter()
        dic[0]=1
        ans=0
        def dfs(node,cur):
            nonlocal ans
            if not node:
                return 
            cur+=node.val
            ans+=dic[cur-targetSum]

            dic[cur]+=1
            dfs(node.left,cur)
            dfs(node.right,cur)
            dic[cur]-=1
        dfs(root,0)
        return ans 

```


very good two sum type problem


use counter to solve two sum problem

why do we backing track the dic but not the cur??

cur will be "backing track" during the recursion

but the dic will not

use backing track to control the fork

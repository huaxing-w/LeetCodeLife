things that easily to make mistake

in the query_tree
```python
def query_tree(self,arr,tree,node,start,end,l,r):
    if start>r or end <l:
        return 0
    if start==end:
        return tree[node]
    if l<=start and end<=r:
        return tree[node]
    mid=(start+end)//2
    left_node=2*node+1
    right_node=2*node+2
    left_sum=self.query_tree(arr,tree,left_node,start,mid,l,r)
    right_sum=self.query_tree(arr,tree,right_node,mid+1,end,l,r)
    return left_sum+right_sum
```

this should be the first exit condition
```python
    if start>r or end <l:
        return 0
```

the range that should return tree[node]
l-------------r
  start---end
this should end the recursion, and return tree[node]

class NumArray:

    def __init__(self, nums: List[int]):
        self.arr=nums
        self.N=len(nums)
        self.tree=[0]*(self.N*4)
        self.build_tree(nums,self.tree,0,0,self.N-1)

    def update(self, index: int, val: int) -> None:
        self.update_tree(self.arr,self.tree,0,0,self.N-1,index,val)

    def sumRange(self, left: int, right: int) -> int:
        return self.query_tree(self.arr,self.tree,0,0,self.N-1,left,right)

    def build_tree(self,arr,tree,node,start,end):
        if start==end:
            tree[node]=arr[start]
            return
        mid=(start+end)//2
        left_node=2*node+1
        right_node=2*node+2
        self.build_tree(arr,tree,left_node,start,mid)
        self.build_tree(arr,tree,right_node,mid+1,end)
        tree[node]=tree[left_node]+tree[right_node]
    
    def update_tree(self,arr,tree,node,start,end,index,val):
        if start==end:
            arr[index]=val
            tree[node]=arr[start]
            return 
        mid=(start+end)//2
        left_node=2*node+1
        right_node=2*node+2

        if index<=mid:
            self.update_tree(arr,tree,left_node,start,mid,index,val)
        else:
            self.update_tree(arr,tree,right_node,mid+1,end,index,val)
        tree[node]=tree[left_node]+tree[right_node]
    
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

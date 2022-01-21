how to do combine by rank??

first you need to have a array with all value =1 to represent the height of tree which is 1

during the union part

always combine the less height tree to the more height tree

```python
def union(x,y):
    temp1=find(x)
    temp2=find(y)
    if temp1!=temp2:
        if rank[temp1]<rank[temp2]:
            parent[temp1]=temp2
        else:
            parent[temp2]=temp1
            if rank[temp1]==rank[temp2]:
                rank[temp1]+=1
```

remember this template

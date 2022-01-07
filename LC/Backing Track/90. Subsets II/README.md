# 2021-01-16
how to elimiate the duplicate subset in an efficient way?
<br>
sort it first
<br>
here comes the tricky part
<br>
```python
for i in range(index, len(nums)):
    if i > index and nums[i] == nums[i - 1]:
        continue
```
we dont just simpily check the nums[i] and nums[i-1]
<br>
we have to include the first one first

>if i > index

this line will do the work.

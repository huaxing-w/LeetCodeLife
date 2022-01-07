# 2022-01-07
the entire code has one shining part
<br>
```python
if visited[j] or (j>0 and nums[j]==nums[j-1] and not visited[j-1]):
     continue
```
so what does that mean?
<br>
when you are in the backing track path, if the visited[i] is true, we should not pick i again
<br>
however, why when it comes to nums[i]==nums[i-1], we dont want to choose the !visited[i] one?
<br>
understand the sequence, what happened first and what happened next
<br>
we are working on ith number right now, when i-1 number is false, and i and i-1 is the same
<br>
it means it just come back from the backing track, we should not go that path again



it is really hard to understand, I could only say I understand 35% of the whole process at this moment.

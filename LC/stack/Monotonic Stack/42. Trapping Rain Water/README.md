
# 2022-01-06
the way to use monotonic stack in the problem is not to find first bigger element or first smaller element
<br/>
but rather simple than the usual monotonic stack problem
<br/>
you just need to have two runs, and maintain the max value at that moment
<br/>
for all the element after, the highest element to its left will be the max one
<br/>
basically, we run the loop from left to right, we find the biggest element of all the right left element
<br/>
and we run the loop from right to left, we find the biggest element of all the left left element
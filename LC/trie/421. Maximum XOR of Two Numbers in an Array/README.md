this is a very good trie type application question

first look at this problem, you want to solve it using two sum method, but we are not trying to find the sum

but the xor, and the max xor has nothing to do with the hash table

now the only way left is N2

however we could use tire to solve this problem

1. trie itself is a hashtable, we log the info from last element 
2. skills, base on the digit of a binary number, how to find the value?
    we are looking at the x digit, if x is 1, ans=ans<<1+1, if x is 0, ans=ans<<1

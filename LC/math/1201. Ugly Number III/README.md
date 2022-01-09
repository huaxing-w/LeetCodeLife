this is actually a pretty hard question

there are many math techniques in here

1. how do you find all prime factor of a number?
  naive way
  ```python
  def primeFactors(n):
    while n % 2 == 0:
        print(2)
        n = n // 2
       
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            print i,
            n = n / i
    if n > 2:
        print n
  ```
  
  python way
  
  ```python
  import primefac
  import sys

  n = int( sys.argv[1] )
  factors = list( primefac.primefac(n) )
  print '\n'.join(map(str, factors))
  ```
2.  how do you find gcd?
    ```python
    def gcd(a, b):
      """Calculate the Greatest Common Divisor of a and b.

      Unless b==0, the result will have the same sign as b (so that when
      b is divided by it, the result comes out positive).
      """
      while b:
          a, b = b, a%b
      return a
    ```
    
    
    ```python
    math.gcd(a,b)
    ```
3.  how do you find lcm?
    ```python
    def lcm(a,b):
      return a*b//math.gcd(a,b)
    
    ```
    ```python
      math.lcm(a,b)
    ```
    
 4. inclusion-exclusion principle
    


   
  

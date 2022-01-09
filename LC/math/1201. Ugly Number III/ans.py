class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:

        def find(x):
            return x//a + x//b + x//c - x//math.lcm(a,b) - x//math.lcm(a,c) - x//math.lcm(b,c) + x//math.lcm(a,b,c)
        l=1
        r=2*pow(10,9)
        while l<r:
            mid=(l+r)//2
            if find(mid)<n:
                l=mid+1
            else:
                r=mid
        return l

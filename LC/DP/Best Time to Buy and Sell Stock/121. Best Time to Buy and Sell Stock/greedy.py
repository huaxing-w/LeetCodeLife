class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_=prices[0]
        ans=0
        for i in prices:
            ans=max(ans,i-min_)
            min_=min(min_,i)
        return ans
        

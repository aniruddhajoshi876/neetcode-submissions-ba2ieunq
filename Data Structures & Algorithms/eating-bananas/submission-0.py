from math import ceil
class Solution:
    def minEatingSpeed(self, piles, h):
        def valid(piles, k, h):
            sum = 0
            for i in piles:
                sum+=ceil(i/k)
            return sum <= h
        l=1
        r=max(piles)

        while l < r:
            mid = (l+r)//2

            if not valid(piles, mid, h):
                l = mid+1
            
            elif valid(piles,mid,h):
                r = mid
        return l
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        def helper(piles, mid):
            hours = 0
            for ele in piles:
                hours += math.ceil(ele/mid)
            return hours
        left = 1
        right = max(piles)
        min_hour = float('inf')
        while(left <= right):
            mid = (left+right)//2
            if helper(piles, mid)<=h:
                min_hour = min(min_hour,mid)
                right = mid-1
            else:
                left = mid+1
        return min_hour
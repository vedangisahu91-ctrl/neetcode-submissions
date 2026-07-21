class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        possible_candidate = 0
        while(left <= right):
            mid = (left+right)//2
            target = mid ** 2
            if target == x:
                return mid
            elif target > x:
                right = mid-1
            else:
                possible_candidate = mid
                left = mid+1
        return possible_candidate

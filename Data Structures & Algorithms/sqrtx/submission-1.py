class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        possible_candidate = 0
        while (left <= right):
            mid = (left + right) // 2
            target = mid ** 2
            if target == x:
                return mid
            elif target < x:
                left  = mid + 1
                possible_candidate = mid
            else:
                right = mid - 1
        return possible_candidate

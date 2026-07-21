class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum_ = 0
        min_len = float('inf')
        i = 0
        j = 0
        while i < len(nums):
            sum_+= nums[i]
            i +=1
            while sum_ >= target and j< len(nums):
                min_len = min(min_len,i-j)
                sum_ -= nums[j]
                j += 1
                
        if min_len == float('inf'):
            return 0
        return min_len

        
        
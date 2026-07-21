class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if max(nums) == 0 or (sum(nums)<0 and max(nums)<0):
            return 1
        for i in range(1,max(nums)):
            if i not in nums:
                return i
        return max(nums)+1
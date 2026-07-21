class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ele = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in ele:
                return [ele[diff],i]
            ele[num] = i
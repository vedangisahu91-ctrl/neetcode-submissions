class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = [False] * len(nums)
        def helper(subarray):
            if len(subarray) == len(nums):
                result.append(subarray.copy())
                return
            for i in range(0, len(nums)):
                if used[i] == True:
                    continue
                subarray.append(nums[i])
                used[i] = True
                helper(subarray)
                subarray.pop()
                used[i] = False
        helper([])
        return result
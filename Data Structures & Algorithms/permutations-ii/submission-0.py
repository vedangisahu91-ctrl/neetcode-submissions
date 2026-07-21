class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        used = [False]*len(nums)
        def helper(subarray):
            if len(subarray) == len(nums):
                res.append(subarray.copy())
                return
            for i in range(0,len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                subarray.append(nums[i])
                used[i] = True
                helper(subarray)
                subarray.pop()
                used[i] = False
        helper([])
        return res
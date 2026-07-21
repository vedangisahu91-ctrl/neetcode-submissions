class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def helper(start,  subarray, sum_):
            if sum_ ==  target:
                result.append(subarray.copy())
                return 
            if sum_ > target:
                return
            for i in range(start, len(nums)):
                subarray.append(nums[i])
                helper(i, subarray, sum_ + nums[i])
                subarray.pop()

        helper(0,[],0)
        return result
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def helper(start,subarray):
            result.append(subarray.copy())
            for i in range(start,len(nums)):
                if i>start and nums[i] == nums[i-1]:
                    continue
                subarray.append(nums[i])
                helper(i+1, subarray)
                subarray.pop()
        helper(0,[])
        return result
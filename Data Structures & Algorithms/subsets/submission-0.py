class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def helper(start, subarray):
            result.append(subarray.copy())

            for i in range(start,len(nums)):
                subarray.append(nums[i])
                helper(i+1,subarray)
                subarray.pop()

        helper(0,[])
        return result
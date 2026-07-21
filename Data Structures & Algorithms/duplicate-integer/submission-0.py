class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict_ = {}
        for i in range(0,len(nums)):
            if nums[i] in dict_.keys():
                return True
            else:
                dict_[nums[i]] = 1
        return False
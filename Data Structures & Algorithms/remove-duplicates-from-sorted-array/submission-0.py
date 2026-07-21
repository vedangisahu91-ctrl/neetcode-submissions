class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # for ele in nums:
        #     dict_[ele] = 1 + dict_.get(ele,0)
        # temp_indx = len(nums)-1
        # count = 0
        # for i in range(len(nums)):
        #     if nums[i] not in dict_.values():
        #         nums[temp_indx] = nums[i]
        #         temp_indx -= 1
        #     else:
        #         count +=1
        # return len(nums)-count

        left = 0
        right = 0
        while right<len(nums):
            if nums[left]!=nums[right]:
                left +=1
                nums[left] , nums[right] = nums[right],nums[left]
            right += 1
        return left+1
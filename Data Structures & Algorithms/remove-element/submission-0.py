class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp_indx = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[temp_indx] = nums[i]
                temp_indx += 1
            else:
                count +=1
        return len(nums)-count
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       counter = 0
       pointer = nums[0]
       for i in range(0,len(nums)):
        if pointer == nums[i]:
            counter += 1
        else:
            counter -= 1
        if counter < 0:
            counter = 1
            pointer = nums[i]
       print(pointer)
       return pointer
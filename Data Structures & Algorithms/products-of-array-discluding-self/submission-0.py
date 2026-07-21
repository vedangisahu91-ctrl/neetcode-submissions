class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1 for i in range(len(nums))]
        left = 1
        for i in range(len(nums)):
            product[i] = left
            left *= nums[i]
        print(product)
        right = 1
        for i in range(len(nums)-1,-1,-1):
            product[i]*=right
            right *= nums[i]
        return product


    # nums = 1 2 4 6
    # prod = 1,1,1,1
    # left = 1,1,2,8
        
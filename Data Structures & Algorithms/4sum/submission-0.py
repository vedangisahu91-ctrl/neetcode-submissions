class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                left = j + 1
                right = len(nums)-1
                while left < right:
                    sum_ = nums[i] +nums[j]+ nums[left] + nums[right]
                    if sum_ == target:
                        res.add((nums[i], nums[j], nums[left] , nums[right]))
                        left += 1
                        right -= 1
                    elif sum_ < target:
                        left += 1
                    else:
                        right -= 1
        return list(res)
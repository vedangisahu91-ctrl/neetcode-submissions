class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        res = set()
        left = 0
        right = 0
        while right < len(nums):
            if right - left > k:
                res.remove(nums[left])
                left += 1
            if nums[right] in res:
                return True
            res.add(nums[right])
            right += 1
        return False
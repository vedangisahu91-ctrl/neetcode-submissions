class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dict_ = {}
        ans = []
        for num in nums:
            dict_[num] = dict_.get(num,0)+1
        compare = len(nums)//3
        for ele, index in dict_.items():
            if index > compare:
                ans.append(ele)
        return ans

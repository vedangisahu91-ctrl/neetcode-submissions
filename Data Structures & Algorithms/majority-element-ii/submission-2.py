class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # dict_ = {}
        # ans = []
        # for num in nums:
        #     dict_[num] = dict_.get(num,0)+1
        # compare = len(nums)//3
        # for ele, index in dict_.items():
        #     if index > compare:
        #         ans.append(ele)
        # return ans
        can1 = 0
        can2 = 0
        count1 = 0
        count2 = 0
        for num in nums:
            if num == can1:
                count1 += 1
            elif num == can2:
                count2 += 1
            elif count1 == 0:
                can1, count1 = num, 1
            elif count2 == 0:
                can2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        
        compare = len(nums)//3
        return [c for c in [can1, can2] if nums.count(c) > compare]
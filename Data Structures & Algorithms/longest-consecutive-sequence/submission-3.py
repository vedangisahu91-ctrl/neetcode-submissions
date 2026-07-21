class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums_set = set(nums)
        # max_length = 0
        # for num in nums_set:
        #     if num-1 not in nums_set:
        #         current = num
        #         count = 1
        #         while current+1 in nums_set:
        #             current += 1
        #             count += 1
        #         max_length = max(max_length,count)
        # return max_length
        max_length = float('-inf')
        for ele in nums:
            if ele + 1 in nums:
                continue
            length = 1
            while(ele - 1 in nums):
                length +=1
                ele = ele -1
            max_length = max(max_length, length)
        return max_length if max_length != float('-inf') else 0
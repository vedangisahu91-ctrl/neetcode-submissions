class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = float('-inf')
        for num in nums:
            if num-1 not in nums:
                current = num
                count =1
                while current+1 in nums:
                    current += 1
                    count += 1
                max_len = max(count,max_len)
        return max_len if max_len > float('-inf') else 0
        # max_length = float('-inf')
        # for ele in nums:
        #     if ele + 1 in nums:
        #         continue
        #     length = 1
        #     while(ele - 1 in nums):
        #         length +=1
        #         ele = ele -1
        #     max_length = max(max_length, length)
        # return max_length if max_length != float('-inf') else 0
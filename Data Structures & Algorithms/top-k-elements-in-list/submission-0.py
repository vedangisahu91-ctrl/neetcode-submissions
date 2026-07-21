class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_ = {}
        for ele in nums:
            dict_[ele] = 1 + dict_.get(ele,0)

        array = [[] for i in range(len(nums))]
        for key, value in dict_.items():
            array[value-1].append(key)
        print(array)
        ans=[]
        for ele in array:
            if ele != []:
                ans.extend(ele)
        return ans[-k:]
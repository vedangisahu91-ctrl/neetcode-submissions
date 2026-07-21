class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def helper(start, subarray, sum_):
            if sum_ == target:
                result.append(subarray.copy())
                return
            if sum_ > target:
                return
            
            for i in range(start,len(candidates)):
                if i> start and candidates[i] == candidates[i-1]:
                    continue
                subarray.append(candidates[i])
                helper(i+1,subarray,sum_ + candidates[i])
                subarray.pop()

        helper(0, [], 0)
        return result
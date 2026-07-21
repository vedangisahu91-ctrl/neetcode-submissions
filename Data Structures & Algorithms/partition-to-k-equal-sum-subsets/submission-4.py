class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        # base case checks
        if total % k != 0:
            return False    

        target = total // k
        buckets = [0] * k
        nums.sort(reverse=True)  # optimization: place larger numbers first

        def backtrack(index):
            # placed all numbers successfully
            if index == len(nums):
                return True

            seen = set()  # avoid trying duplicate bucket values
            #used = [False]*len(nums)
            for i in range(k):
                # skip if adding nums[index] exceeds target
                if buckets[i] + nums[index] > target:
                    continue
                # skip duplicate bucket states
                if buckets[i] in seen:
                    continue

                seen.add(buckets[i])
                buckets[i] += nums[index]
                if backtrack(index + 1):
                    return True
                buckets[i] -= nums[index]  # backtrack

            return False
        return backtrack(0)
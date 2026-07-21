class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [x for x in range(1,n+1)]
        result = []
        print(arr)

        def helper(start,subarray):
            if len(subarray) == k:
                result.append(subarray.copy())
                return
            for  i in range(start,len(arr)):
                subarray.append(arr[i])
                helper(i+1, subarray)
                subarray.pop()

        helper(0,[])
        return result
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def sort(arr):
            if len(arr)<=1:
                return arr
            pivot = arr[len(arr)//2]
            left = []
            right = []
            middle = []
            for ele in range(len(arr)):
                if pivot> arr[ele]:
                    left.append(arr[ele])
                elif pivot < arr[ele]:
                    right.append(arr[ele])
                else:
                    middle.append(arr[ele])
            return sort(left) + middle + sort(right)
        return(sort(nums))   
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)-1
        while(left<=right):
            mid = (left+right)//2
            if (matrix[mid][0] <= target and matrix[mid][-1] >= target):
                inner_left = 0
                inner_right = len(matrix[mid])-1

                while(inner_left <= inner_right):
                    inner_mid = (inner_left+inner_right )  // 2
                    if matrix[mid][inner_mid] == target:
                        return True
                    elif  matrix[mid][inner_mid] < target:
                        inner_left = inner_mid+1
                    else:
                        inner_right = inner_mid-1
                return False
            elif matrix[mid][-1] < target:
                left = mid+1
            else:
                right = mid-1
        return False

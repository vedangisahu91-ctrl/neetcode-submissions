class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_ = [0 for _ in range(26)]
        for ele in s:
            list_[ord(ele) - ord('a')] +=1
        for indx, ele in enumerate(t):
            list_[ord(ele) - ord('a')] -=1
        for val in list_:
            if val != 0:
                return False
        return True
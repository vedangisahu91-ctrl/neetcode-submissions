class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_ = [ 0 for _ in range(26)]
        for i in s:
            list_[ord(i) - ord('a')] += 1
        print(list_)
        for i in t:
            list_[ord(i) - ord('a')] -= 1
        print(list_)
        
        for val in list_:
            if val !=  0:
                return False
        return True
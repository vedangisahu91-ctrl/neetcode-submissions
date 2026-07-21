class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def helper(start, substring):
            if start == len(s):
                res.append(substring.copy())
                return
            for i in range(start, len(s)):
                if isPalindrome(s, start, i):
                    substring.append(s[start:i+1])
                    helper(i+1, substring)
                    substring.pop()
        helper(0,[])
        return res
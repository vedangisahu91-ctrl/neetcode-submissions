class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome(s, left, right):
            while(left<= right):
                if s[right] != s[left]:
                    return False
                left += 1
                right -= 1
            return True
        left = 0
        right = len(s)-1
        while(left<=right):
            if s[right] == s[left]:
                left += 1
                right -= 1
            else:
                return palindrome(s,left+1, right) or palindrome(s, left, right-1)
        return True
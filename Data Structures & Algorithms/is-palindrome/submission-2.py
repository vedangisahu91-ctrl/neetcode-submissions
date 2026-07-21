class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s =""
        for i in s:
            if i.isalnum():
                new_s += i.lower()
        reverse_s = new_s[::-1]
        if new_s == reverse_s:
            return True
        return False
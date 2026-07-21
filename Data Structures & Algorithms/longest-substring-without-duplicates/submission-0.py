class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = ""
        left = 0
        right = 0
        longest = 0
        while right < len(s):
            if s[right] not in string:
                string += s[right]
            else:
                while left < right and s[right] in string:
                    string = string[1:]
                    left += 1
                string += s[right]
            longest = max(longest, len(string))
            right += 1
        return longest

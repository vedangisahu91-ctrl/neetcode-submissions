class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        common_prefix = ""
        first = strs[0]
        last = strs[len(strs)-1]
        for i in range(len(first)):
            if i< len(last) and first[i]==last[i]:
                common_prefix += first[i]
            else:
                break

        return common_prefix

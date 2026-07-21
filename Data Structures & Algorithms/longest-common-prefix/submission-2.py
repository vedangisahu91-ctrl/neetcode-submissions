class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first = strs[0]
        store = ""
        for i in range(len(first)):
            if first[i] == strs[-1][i]:
                store = store + first[i]
            else:
                break
        return store

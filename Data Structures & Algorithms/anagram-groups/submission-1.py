class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_ = {}
        for i in strs:
            sorted_i = "".join(sorted(i))
            if sorted_i in dict_.keys():
                dict_[sorted_i].append(i)
            else:
                dict_[sorted_i]=[i]
        values = list(dict_.values())
        return values
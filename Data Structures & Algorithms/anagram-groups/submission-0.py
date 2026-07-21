class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp = {}
        for i in strs:
            key = "".join(sorted(i))
            if key not in grp:
                grp[key] = [i]
            else:
                grp[key].append(i)
            print(grp)
        value_list = list(grp.values())
        return value_list

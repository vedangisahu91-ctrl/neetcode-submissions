class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for i in strs:
            string += f"{len(i)}#"+ i
        print(string)
        return string

    def decode(self, s: str) -> List[str]:
        decode_list = []
        lenght = 0
        i = 0
        while(i<len(s)):
            j=i
            while(s[j] != '#'):
                j += 1
            lenght = int(s[i:j])
            word = s[j+1:j+1+lenght]
            decode_list.append(word)
            i = j+1+lenght
        return decode_list
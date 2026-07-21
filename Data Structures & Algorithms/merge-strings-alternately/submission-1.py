class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_string = ""
        min_len_s = min(word1,word2)
        count1, count2 = 0,0
        for i in range(len(min_len_s)):
            if i < len(word1):
                new_string += word1[i]
                count1 +=1
            if i < len(word2):
                new_string += word2[i]
                count2 +=1
        if len(word1) > count1:
            new_string = new_string+word1[count1:]
        if len(word2) > count2:
            new_string = new_string+word2[count2:]

        return new_string
            
        
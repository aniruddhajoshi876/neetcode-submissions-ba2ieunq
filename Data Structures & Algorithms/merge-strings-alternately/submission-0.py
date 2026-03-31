class Solution:
    def mergeAlternately(self, word1, word2):
        word3 = ''

        n = min(len(word1), len(word2))
        m=0
        while n > 0:
            word3 += word1[m] + word2[m]
            m+=1
            n-=1
        if len(word1) > len(word2):
            return word3 + word1[m::]
        if len(word1) < len(word2):
            return word3 + word2[m::]
        if len(word1) == len(word2):
            return word3

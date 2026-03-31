class Solution:
    def groupAnagrams(self, strs):
        seen = {}
        res= []
        for w in strs:
            freq = [0] * 26
            for i in w:
                freq[ord(i)-ord('a')]+=1
            if tuple(freq) in seen:
                seen[tuple(freq)].append(w)
            else:
                seen[tuple(freq)] = [w]

        res= [l for l in seen.values()]
        return res 
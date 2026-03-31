class Solution:
    def characterReplacement(self, s, k) :
        l=0
        seen={}
        maxf=0
        maxl=0
        for r in range(len(s)):
            seen[s[r]] = 1 + seen.get(s[r],0)
            maxf = max(seen.values())

            if r-l+1 - maxf > k:
                seen[s[l]]-=1
                l+=1
            maxl=max(maxl, r-l+1)
        return maxl
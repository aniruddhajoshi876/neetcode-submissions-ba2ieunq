class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = []
        max_len = 0
    
        for r in range(len(s)):
            while s[r] in seen:
                seen=seen[1::]
                l+=1
            seen.append(s[r])
            max_len = max(max_len, r-l+1)
        return max_len
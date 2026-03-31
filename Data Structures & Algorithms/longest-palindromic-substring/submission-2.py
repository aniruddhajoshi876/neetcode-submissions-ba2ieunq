class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        res = ''
        reslen = 0

        for i in range(n):
            j=i
            k=i
            while (j < n and k >= 0) and s[j] == s[k]:
                if (j+1 - k) > reslen:
                    res = s[k:j+1]
                    reslen= j+1-k
                j+=1
                k-=1
            
                
            left = i+1
            right = i

            while left < n and right >= 0 and s[right] == s[left]:
                
                if (left+1-right) > reslen:
                    res = s[right:left+1]
                    reslen = left+1-right

                left+=1
                right-=1
        
        return res
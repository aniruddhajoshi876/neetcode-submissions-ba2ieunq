class Solution:
    def partition(self, s):
        def is_palindrome(word):
            return word == word[::-1]
        
        res = []
        subset = []
        def dfs(j):

            if j >= len(s):
                res.append(subset.copy())
                return
            for i in range(j, len(s)):

                if is_palindrome(s[j:i+1]):
                    subset.append(s[j:i+1])
                    dfs(i+1)
                    subset.pop()
        dfs(0)
        return res
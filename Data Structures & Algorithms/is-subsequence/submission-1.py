class Solution:
    def isSubsequence(self, s, t):
        pos = 0
        for i in range(len(s)):
            if t.find(s[i],pos) == -1:
                return False
            pos = t.find(s[i])
        return True
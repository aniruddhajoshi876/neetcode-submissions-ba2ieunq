class Solution:
    def isAnagram(self, s, t):
        zs ={}
        zt = {}
        for i in s:
            zs[i] = zs.get(i, 0) + 1
        for j in t:
            zt[j] = zt.get(j, 0) + 1
        return zs == zt

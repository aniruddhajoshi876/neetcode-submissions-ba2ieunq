class Solution:
    def countSubstrings(self, s):
        res = []
        n = len(s)
        for i in range(n):
            left1 = i
            right1=i
            while left1 < n and right1 >= 0 and s[left1] == s[right1]:
                res.append(s[right1:left1+1])
                left1+=1
                right1-=1

            left2 = i+1
            right2=i
            while left2 < n and right2 >= 0 and s[left2] == s[right2]:
                res.append(s[right2:left2+1])
                left2+=1
                right2-=1
        
        return len(res)
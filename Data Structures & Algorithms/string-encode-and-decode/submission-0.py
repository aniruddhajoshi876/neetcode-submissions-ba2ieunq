class Solution:

    def encode(self, strs):
        
        code = ''
        if not strs:
            return code
        for i in strs:
            code = code + str(len(i))+'#'+i
        return code
    
    def decode(self, s):
        res=[]
        i=0
        while i < len(s):
            num=''
            while s[i] != '#' and s[i].isdigit():
                num+=s[i]
                i+=1
            res.append(s[i+1:i+1+int(num)])
            i=1+i+int(num)
        return res
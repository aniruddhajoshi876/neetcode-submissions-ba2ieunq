class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        if s1==s2:
            return True
        f1 ={}
        f2 = {}
        for i in 'abcdefghijklmnopqrstuvwxyz':
            f1[i] = 0
            f2[i]=0
        window = len(s1)
        for i in range(len(s1)):
            f1[s1[i]]+=1
            f2[s2[i]]+=1
        l=0
        if f1 == f2:
                return True
        for r in range(len(s1),len(s2)):
            #if f1 == f2:
                #return True
            f2[s2[r]]+=1
            f2[s2[l]]-=1
            l+=1
            if f1 == f2:
                return True
        return False
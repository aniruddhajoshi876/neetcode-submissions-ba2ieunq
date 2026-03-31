class Solution:
    def isValid(self, s):
        z = []
        check = {')':'(', '}':'{', ']':'['}
        for i in s:
            if i in '[{(':
                z.append(i)
            if i in ']})':
                if len(z)==0 or z[-1] != check[i]:
                    return False
                else:
                    z.pop()
        return not z
class Solution:
    def carFleet(self, target, position, speed):
        z= [(p,s) for p,s in zip(position, speed)]
        res = [0]*len(z)
        z.sort(reverse=True)
        stack=[]
        for p,s in z:
            stack.append((target-p)/s)
            while len(stack)>=2 and stack[-2] >= stack[-1]:
                stack.pop()
            
        return len(stack)

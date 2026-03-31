class Solution:
    def evalRPN(self, tokens):
        nums = []
        calc=int(tokens[0])
        for i in tokens:
            if i.isdigit() or i[1::].isdigit():
                nums.append(i)

            else:
                v1=int(nums.pop()) #second num
                v2=int(nums.pop()) #first num
                if i =='+':
                    calc = v2 + v1
                    nums.append(calc)
                elif i == '-':
                    calc = v2-v1
                    nums.append(calc)
                elif i=='/':
                    calc=v2/v1
                    nums.append(int(calc))
                elif i == '*':
                    calc = v2*v1
                    nums.append(calc)
        return int(calc)
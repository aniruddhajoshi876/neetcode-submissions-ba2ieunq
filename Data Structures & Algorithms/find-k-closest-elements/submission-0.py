class Solution:
    def findClosestElements(self, arr, k, x):
        start = 0
        window =  arr[0:k]

        def closerthan(x,a,b):
            if (abs(a-x) < abs(b-x)) or (abs(a-x) == abs(b-x) and a < b):
                return True
            return False

        
        for end in range(2,len(arr)):

            while closerthan(x, arr[end], window[0]) and len(window)==k and arr[end] not in window:
                window.pop(0)
                start+=1
                window.append(arr[end])

        return window
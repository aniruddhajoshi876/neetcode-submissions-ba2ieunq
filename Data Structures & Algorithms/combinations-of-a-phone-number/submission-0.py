class Solution:
    def letterCombinations(self, digits):
        vocab = {2: ['a','b', 'c'], 3:['d', 'e', 'f'], 4:['g','h', 'i'], 5:['j','k','l'], 6:['m','n','o'],
                 7: ['p','q','r','s'], 8:['t','u','v'], 9:['w','x','y','z']}
        if not digits:
            return []
        res = []
        subset = []
        def dfs(index):

            if index >= len(digits):
                res.append(''.join(subset))
                return
            for i in vocab[int(digits[index])]:
                subset.append(i)
                dfs(index+1)
                subset.pop()
        dfs(0)
        return res
                

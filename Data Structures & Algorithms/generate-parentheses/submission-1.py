class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = []

        def dfs(open,close):
            if len(subset) == 2*n and open == n:
                res.append(''.join(subset))
                return
            if close > open:
                return
            if open < n:
                subset.append('(')
                dfs(open+1, close)
                subset.pop()
            if close < open:
                subset.append(')')
                dfs(open,close+1)
                subset.pop()
        dfs(0,0)
        return res
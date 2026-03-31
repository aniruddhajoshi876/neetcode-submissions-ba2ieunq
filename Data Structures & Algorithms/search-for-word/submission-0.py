class Solution:
    def exist(self, board, word):
        seen = set()
        moves = [(1,0), (0,1), (-1,0), (0,-1)]
        length = len(board)
        width = len(board[0])
        def dfs(index, row, col):
            if row >= length or row < 0 or col < 0 or col >= width:
                return False
            if 0 <= row < length and 0<= col < width and word[index] == board[row][col] and index == len(word)-1:
                return True
            
            if word[index] != board[row][col]:
                return False
            
            res = False
            seen.add((row, col))
            for dx, dy in moves:

                if (row + dx, col + dy) in seen:
                    continue

                res = dfs(index + 1, row +dx, col + dy)
                if res:
                    break
            seen.remove((row, col))
            return bool(res)
        for i in range(length):
            for j in range(width):
                cap = dfs(0,i,j)
                if cap:
                    return True
        return False
        
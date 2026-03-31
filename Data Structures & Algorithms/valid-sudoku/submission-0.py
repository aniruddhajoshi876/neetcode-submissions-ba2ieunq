class Solution:
    def isValidSudoku(self, board):
        def valid_rows(config):
            for i in config:
                count = {}
                for j in i:
                    if j in '123456789':
                        count[j] = 1 + count.get(j,0)
                        if count[j] > 1:
                            return False
            return True
        
        def valid_cols(config):
            for i in range(len(config)):
                count = {}
                for j in range(len(config)):
                    if config[j][i] in '123456789':
                        count[config[j][i]] = 1 + count.get(config[j][i],0)
                        if count[config[j][i]] > 1:
                            return False
            return True

        def valid_squares(config):
            for row in range(0,9,3):
                for col in range(0,9,3):
                    count = {}
                    for i in range(3):
                        for j in range(3):
                            val = config[row+i][col+j]
                            if val in '123456789':
                                count[val] = 1 + count.get(val,0)
                                if count[val] > 1:
                                    return False
            return True
        return valid_rows(board) and valid_cols(board) and valid_squares(board)
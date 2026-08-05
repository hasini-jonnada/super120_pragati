class Solution(object):
    def isValidSudoku(self, board):
        def not_valid(row,col,val):
            for i in range(row+1,9):
                if val == board[i][col]:
                    return True
            for i in range(col+1,9):
                if val == board[row][i]:
                    return True
            i ,j = (row//3)*3,(col//3)*3
            for r in range(i,i+3):
                for c in range(j,j+3):
                    if board[r][c]!= val and (r,c)!=(row,col) :
                        return True
            return False
        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    if not_valid(row,col,board[row][col]):
                        return False
        return True

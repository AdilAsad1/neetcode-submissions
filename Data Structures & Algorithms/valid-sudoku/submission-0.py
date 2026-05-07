class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            s = set(x for x in i if x != '.')
            a = [x for x in i if x != '.']
            if len(s) != len(a):
                return False

        for i in range(len(board)):
            a = []
            for j in board:
                if j[i] != '.':
                    a.append(j[i])
            s = set(a)
            if len(s) != len(a):
                return False
            
        for box_row in range(3):
            for box_col in range(3):
                a = []
                for r in range(box_row*3, box_row*3 + 3):
                    for c in range(box_col*3, box_col*3 + 3):
                        if board[r][c] != '.':
                            a.append(board[r][c])
                s = set(a)
                if len(s) != len(a):
                    return False

        return True
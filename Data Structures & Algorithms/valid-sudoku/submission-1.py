class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for r in board:
            rowset = set()
            for i in r:
                if i == ".":
                    continue
                elif i in rowset:
                    return False
                else:
                    rowset.add(i)
        # check cols
        for col in zip(*board):
            colset = set()
            for i in col:
                if i == ".":
                    continue
                elif i in colset:
                    return False
                else:
                    colset.add(i)
        for r in range(0, 3):
            for c in range(0, 3):
                sset = set()
                for i in range(0, 3):
                    for j in range(0, 3):
                        x = r * 3 + i
                        y = c * 3 + j
                        if board[x][y] == ".":
                            continue
                        elif board[x][y] in sset:
                            return False
                        else:
                            sset.add(board[x][y])
    
        return True
                    
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            mp = [0] * 10
            for v in row:
                if v != ".":
                    if mp[int(v)] > 0:
                        return False
                    mp[int(v)] = 1
        for col in zip(*board):
            mp = [0] * 10
            for v in col:
                if v != ".":
                    if mp[int(v)] > 0:
                        return False
                    mp[int(v)] = 1
        for r in range(3):
            for c in range(3):
                mp = [0] * 10
                for rc in range(3):
                    rn = r * 3 + rc
                    for cc in range(3):
                        cn = c * 3 + cc
                        if board[rn][cn] != ".":
                            if mp[int(board[rn][cn])] > 0:
                                return False
                            mp[int(board[rn][cn])] = 1
        return True


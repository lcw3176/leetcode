class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            temp_set = set()
            temp_lst = list()

            for i in row:
                if i != ".":
                    temp_set.add(i)
                    temp_lst.append(i)

            if len(temp_set) != len(temp_lst):
                return False

        for i in range(0, len(board)):
            temp_set = set()
            temp_lst = list()

            for j in range(0, len(board[i])):
                if board[j][i] != ".":
                    temp_set.add(board[j][i])
                    temp_lst.append(board[j][i])

            if len(temp_set) != len(temp_lst):
                return False

        for i in range(0, len(board), 3):
            
            
            for offset in range(0, len(board), 3):
                temp_lst = list()
                temp_set = set()

                for j in range(3):
                    for k in range(3):
                        if board[i + j][k + offset] != ".":
                            temp_lst.append(board[i + j][k + offset])
                            temp_set.add(board[i + j][k + offset])

                if len(temp_lst) != len(temp_set):
                    return False

        return True
            
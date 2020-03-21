
def find_zero(board):
    for irow, row in enumerate(board):
        for icol, col in enumerate(row):
            if col == 0:
                return irow, icol

    return 10, 10


def is_valid(board, n, row, col):
    for i in range(len(board)):
        if board[row][i] == n and i != col:
            return False
    for j in range(len(board[row])):
        if board[j][col] == n and j != row:
            return False
    coord = (row//3, col//3)

    for i in range(coord[0]*3, coord[0]*3+2):
        for j in range(coord[1]*3, coord[1]*3+2):
            if board[i][j] == n and (i != row and j != col):
                return False
    return True


def solve(board):
    row, col = find_zero(board)
    if row == 10 and col == 10:
        print("Solucionado!")
        print_board(board)
        return True
    for n in range(1, 10):
        if is_valid(board, n, row, col):
            board[row][col] = n
            if solve(board) is True:
                return True
            else:
                board[row][col] = 0
        else:
            continue
    return False


def print_board(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            print(board[row][col], end=" ")
            if (col+1) % 3 == 0 and col+1 != 9:
                print("| ", end="")
            if col+1 == 9:
                print()
        if (row+1) % 3 == 0 and row+1 != 9:
            print("-"*21)


board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

if __name__ == "__main__":
    print_board(board)
    # print(find_zero(board))
    # row, col = find_zero(board)
    # print(is_valid(board, 7, row, col))
    print(solve(board))

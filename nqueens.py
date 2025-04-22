def print_solution(board, n):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col]:  
            return False
        if col - (row - i) >= 0 and board[i][col - (row - i)]:  # Check left diagonal
            return False
        if col + (row - i) < n and board[i][col + (row - i)]:  # Check right diagonal
            return False
    return True

def solve_n_queens(board, row, n):
    if row == n:
        print_solution(board, n)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens(board, row + 1, n)
            board[row][col] = 0  # backtrack

n = int(input("Enter the number of queens: "))
board = [[0] * n for _ in range(n)]
solve_n_queens(board, 0, n)

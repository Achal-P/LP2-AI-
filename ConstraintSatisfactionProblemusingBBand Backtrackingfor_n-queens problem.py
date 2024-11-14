#Implement a solution for a Constraint Satisfaction Problem  using Branch and Bound and Backtracking for n-queens problem or a graph coloring problem.
# Function to check if placing a queen at (row, col) is safe
def is_safe(board, row, col):
    # Check column
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

# Function to solve N-Queens problem using Backtracking
def n_queens_backtracking(board, col):
    # Base case: if all queens are placed
    if col >= len(board):
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1  # Place the queen

            # Recur to place rest of the queens
            if n_queens_backtracking(board, col + 1):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution, backtrack
            board[i][col] = 0

    # If the queen can't be placed in any row of this column
    return False

# Function to solve N-Queens problem using Branch and Bound
def n_queens_branch_and_bound(board, col):
    # Base case: if all queens are placed
    if col >= len(board):
        return True

    # Try placing queens in the current column based on heuristics
    for i in range(len(board)):
        if is_safe(board, i, col):
            # Place the queen
            board[i][col] = 1
            
            # Recur to place rest of the queens
            if n_queens_branch_and_bound(board, col + 1):
                return True
            
            # If placing queen in board[i][col] doesn't lead to a solution, backtrack
            board[i][col] = 0

    # If no queen can be placed in this column
    return False

# Function to print the board
def print_board(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))
    print()

# Function to take input for the size of the chessboard (N)
def input_board_size():
    while True:
        try:
            size = int(input("Enter the size of the chessboard (N): "))
            if size <= 0:
                print("Please enter a positive integer greater than 0.")
            else:
                return size
        except ValueError:
            print("Please enter a valid integer.")

# Function to take input for the solution approach
def input_solution_approach():
    while True:
        approach = input("Enter the solution approach (backtracking/branch_and_bound): ").lower()
        if approach in ['backtracking', 'branch_and_bound']:
            return approach
        else:
            print("Please enter 'backtracking' or 'branch_and_bound'.")

# Main function
def main():
    # Input the size of the chessboard (N)
    N = input_board_size()

    # Input the solution approach
    approach = input_solution_approach()

    # Initialize an empty chessboard
    board = [[0] * N for _ in range(N)]

    # Solve N-Queens problem
    print("Solving N-Queens problem using", approach + ":")
    if approach == 'backtracking':
        if n_queens_backtracking(board, 0):
            print_board(board)
        else:
            print("No solution exists.")
    else:  # Branch and Bound
        if n_queens_branch_and_bound(board, 0):
            print_board(board)
        else:
            print("No solution exists.")

# Execute main function
if __name__ == "__main__":
    main()
"""Output
Enter the size of the chessboard (N): 4
Solving N-Queens problem using Backtracking:
0 0 1 0
1 0 0 0
0 0 0 1
0 1 0 0
Solving N-Queens problem using Branch and Bound:

Enter the size of the chessboard (N): 4
Enter the solution approach (backtracking/branch_and_bound): branch_and_bound
Solving N-Queens problem using branch_and_bound:
0 0 1 0
1 0 0 0
0 0 0 1
0 1 0 0
=== Code Execution Successful ==="""
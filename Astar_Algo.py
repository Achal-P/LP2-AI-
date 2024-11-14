#A* Algorithm 
import heapq

# Function to calculate the Manhattan distance between two points
def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

# Function to find the position of a number in the board
def find_number(board, number):
    for i in range(3):
        for j in range(3):
            if board[i][j] == number:
                return i, j

# Function to generate possible moves from the current state
def generate_moves(board):
    moves = []
    x, y = find_number(board, 0)  # Find the position of the blank tile (0)
    if x > 0:   # Move blank tile up
        new_board = [row[:] for row in board]
        new_board[x][y], new_board[x - 1][y] = new_board[x - 1][y], new_board[x][y]
        moves.append(new_board)
    if x < 2:   # Move blank tile down
        new_board = [row[:] for row in board]
        new_board[x][y], new_board[x + 1][y] = new_board[x + 1][y], new_board[x][y]
        moves.append(new_board)
    if y > 0:   # Move blank tile left
        new_board = [row[:] for row in board]
        new_board[x][y], new_board[x][y - 1] = new_board[x][y - 1], new_board[x][y]
        moves.append(new_board)
    if y < 2:   # Move blank tile right
        new_board = [row[:] for row in board]
        new_board[x][y], new_board[x][y + 1] = new_board[x][y + 1], new_board[x][y]
        moves.append(new_board)
    return moves

# Function to solve the 8 puzzle problem using A* algorithm
def solve_puzzle(start, goal):
    # Priority queue to store states with th   eir costs
    open_list = [(0 + manhattan_distance(*find_number(start, 0), *find_number(goal, 0)), start)]
    closed_list = set()
    iterations = 0

    while open_list:
        # Pop the state with the lowest cost from the priority queue
        cost, current = heapq.heappop(open_list)
        iterations += 1
        if current == goal:
            return current, iterations
        
        # Add current state to the closed list
        closed_list.add(tuple(map(tuple, current)))

        # Generate possible moves from the current state
        moves = generate_moves(current)
        for move in moves:
            if tuple(map(tuple, move)) not in closed_list:
                # Calculate cost for the move and add it to the priority queue
                move_cost = cost + 1 + manhattan_distance(*find_number(move, 0), *find_number(goal, 0))
                heapq.heappush(open_list, (move_cost, move))

# Function to take input for the state of the puzzle
def input_state(prompt):
    print(prompt)
    state = []
    for i in range(3):
        row = list(map(int, input().split()))
        state.append(row)
    return state

# Function to print the board
def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

# Main function
def main():
    # Input the initial and goal states of the puzzle
    initial_state = input_state("Enter the initial state of the puzzle (3x3 board with numbers 0-8, use 0 for blank tile):")
    goal_state = input_state("Enter the goal state of the puzzle (3x3 board with numbers 0-8, use 0 for blank tile):")

    print("Initial state:")
    print_board(initial_state)
    print("Goal state:")
    print_board(goal_state)

    # Solve the puzzle using A* algorithm
    solution, iterations = solve_puzzle(initial_state, goal_state)
    print("Solution:")
    print_board(solution)
    print("Number of iterations required:", iterations)

# Execute main function
if __name__ == "__main__":
    main()
"""output
Enter the initial state of the puzzle (3x3 board with numbers 0-8, use 0 for blank tile):
2 8 3 
1 6 4 
7 0 5 
Enter the goal state of the puzzle (3x3 board with numbers 0-8, use 0 for blank tile):
1 2 3 
8 0 4 
7 6 5
Initial state:
2 8 3
1 6 4
7 0 5
Goal state:
1 2 3
8 0 4
7 6 5
Solution:
1 2 3
8 0 4
7 6 5
Number of iterations required: 32
=== Code Execution Successful ==="""
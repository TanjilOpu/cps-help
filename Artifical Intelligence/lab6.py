import copy
N = 3
class p8_board:
    def __init__(self,board,x,y):
        self.board = board
        self.x=x
        self.y=y
        self.h = manhattan(board)
goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]

row = [0, 0, -1, 1]
col = [-1, 1, 0, 0]

def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N

def manhattan(board):
    distance = 0
    for i in range(N):
        for j in range(N):
            val = board[i][j]
            if val != 0:
                goal_x = (val - 1) // N
                goal_y = (val - 1) % N
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

def print_board(board):
    for r in board:
        print(r)
    print()

def is_solvable(board):
    flat = []
    for row in board:
        for num in row:
            if num != 0:
                flat.append(num)
    inversions = 0
    for i in range(len(flat)):
        for j in range(i + 1, len(flat)):
            if flat[i] > flat[j]:
                inversions += 1
    return inversions % 2 == 0


def solve(start, x, y):
    if not is_solvable(start):
        print("Puzzle is unsolvable")
        return
    current = p8_board(start,x,y)
    while True:
        print("Current heuristic value",current.h)
        print_board(current.board)
        if current.board==goal:
            print("solution found")
            return 
        
        best_neighbour = None
        best_h=current.h

        for i in range(4):
            new_x = current.x+row[i]
            new_y = current.y+col[i]
            if is_valid(new_x,new_y):
                new_board = copy.deepcopy(current.board)
                new_board[current.x][current.y],new_board[new_x][new_y] =\
                    new_board[new_x][new_y],new_board[current.x][current.y]
                h=manhattan(new_board)
                if h<best_h:
                    best_h = h
                    best_neighbour=p8_board(new_board,new_x,new_y)
        if best_neighbour is None:
            print("Stuc at local minimumm ")
            return
        current=best_neighbour
    
start = [[1, 2, 3],
         [5, 0, 8],
         [7, 4, 6]]
x, y = 1, 1
solve(start, x, y)

import copy
N=3
row = [0, 0, -1, 1]
col = [-1, 1, 0, 0]

class p8_board:
    def __init__(self,board,x,y,depth):
        self.board = board
        self.x=x
        self.y=y
        self.depth=depth

def is_solveable(board):
    flat = []
    for row in board:
        for num in row:
            if num!=0:
                flat.append(num)
    inversion = 0
    for i in range(len(flat)):
        for j in range(i+1,len(flat)):
            if flat[i]>flat[j]:
                inversion+=1
    return inversion%2==0


def is_goal(board):
    goal = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]]
    return goal == board

def print_board(board):
    for row in board:
        print(row)

def is_valid(x,y):
    return 0<=x<N and 0<=y<N

def solve(start,x,y,max_depth=0):

    if not is_solveable(start):
        print("Not solveable this problem")
        return 
    # queue = deque()
    stack = []
    visited = set()
    stack.append(p8_board(start,x,y,0))
    while stack:
        current = stack.pop()
        board_tuple = tuple(tuple(r) for r in current.board)
        if board_tuple in visited:
            continue
        visited.add(board_tuple)

        if(current.depth>=max_depth):
            continue

        if is_goal(current.board):
            print("solution found at depth: ",current.depth)
            print_board(current.board)
            return 
        
    
        
        for i in range(4):
            new_x = current.x+row[i]
            new_y = current.y+col[i]

            if is_valid(new_x,new_y):
                new_board = copy.deepcopy(current.board)
                new_board[current.x][current.y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[current.x][current.y]
                stack.append(p8_board(new_board,new_x,new_y,current.depth+1))

    print(f"No solution found at limit {max_depth}")

start = [[1, 2, 3],
        [4, 5, 6],
        [7, 0, 8]]
x,y = 2,1
solve(start,x,y,20)
import heapq
import copy
N=3
row = [0, 0, -1, 1]
col = [-1, 1, 0, 0]

class p8_board:
    def __init__(self,board,x,y,g,parent=None):
        self.board = board
        self.x = x
        self.y = y
        self.g = g
        self.h = manhatten(board)
        self.f = self.g + self.h
        self.parent=parent
    
    def __lt__(self,other):
        return self.f<other.f
    
def manhatten(board):
    distance = 0
    for i in range(N):
        for j in range(N):
            val = board[i][j]
            if val!=0:
                goal_x = (val -1)//N
                goal_y = (val -1)%N
                distance+= abs(goal_x - i) + abs(goal_y - j)
    return distance

def is_solveable(board):
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

def is_goal(board):
    goal =  [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 0]]
    return goal == board

def print_board(board):
    for r in board:
        print(r)

def print_path(node):
    path = []
    while node:
        path.append(node.board)
        node  = node.parent
    
    path.reverse()
    print("Solution path:")
    step = 0
    for board in path:
        print("step: ",step)
        print_board(board)
        step+=1

def is_valid(x,y):
    return 0<=x<N and 0<=y<N

def solve(start,x,y):
    if not is_solveable(start):
        print("Puzzle is not solveable")
        return
    
    pq = []
    visited = set()
    heapq.heappush(pq,p8_board(start,x,y,0))

    while pq:
        current = heapq.heappop(pq)
        board_tuple = tuple(tuple(r) for r in current.board)

        if board_tuple in visited:
            continue
        visited.add(board_tuple)

        if is_goal(current.board):
            print("solution found at depth ",current.g)
            print("Solution found cost ",current.f)
            print("solution cost manhatten ",current.h)
            # print_board(current.board)
            print_path(current)
            return

        for i in range(4):
            new_x = current.x+row[i]
            new_y = current.y+col[i]

            if is_valid(new_x,new_y): 
                new_board = copy.deepcopy(current.board)
                new_board[current.x][current.y],new_board[new_x][new_y] = new_board[new_x][new_y],new_board[current.x][current.y]
                heapq.heappush(pq,p8_board(new_board,new_x,new_y,current.g +1, current))
    print("Solution not found ")        
start = [[1, 2, 3],
         [4, 5, 6],
         [7, 0, 8]]
x, y = 2, 1
solve(start, x, y)

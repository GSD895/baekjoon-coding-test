from collections import deque

def bead_escape(board, n, m):
    # Find the starting position of the red bead
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start_x, start_y = i, j
                break

    # BFS queue to store the states of the board
    queue = deque()
    queue.append((start_x, start_y, 0))  # store the starting position and the number of moves
    visited = set()  # set to store the visited states

    # define the possible movements
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y, moves = queue.popleft()

        # check if the red bead has reached the hole
        if board[x][y] == 'O':
            return moves

        # mark the current state as visited
        visited.add((x, y))

        # perform the possible movements
        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
            if 0 <= new_x < n and 0 <= new_y < m:
                if board[new_x][new_y] != '#' and board[new_x][new_y] != 'B' and (new_x, new_y) not in visited:
                    queue.append((new_x, new_y, moves + 1))

    # if the red bead cannot be pulled out through the hole
    return -1

# example usage
board = [['#', '#', '#', '#', '#'],
         ['#', '.', '.', 'B', '#'],
         ['#', '.', '#', '.', '#'],
         ['#', 'R', 'O', '.', '#'],
         ['#', '#', '#', '#', '#']]
n, m = 5, 5
print(bead_escape(board, n, m))
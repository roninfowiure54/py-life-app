import time
import os

def render_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in board:
        print("".join(["#" if cell else " " for cell in row]))

def get_next_generation(board):
    h, w = len(board), len(board[0])
    next_board = [[False]*w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            neighbors = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0: continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < h and 0 <= nc < w and board[nr][nc]:
                        neighbors += 1
            if board[r][c] and neighbors in [2, 3]:
                next_board[r][c] = True
            elif not board[r][c] and neighbors == 3:
                next_board[r][c] = True
    return next_board

def main():
    h, w = 10, 20
    board = [[False]*w for _ in range(h)]
    # Glider pattern
    board[1][2] = board[2][3] = board[3][1] = board[3][2] = board[3][3] = True
    
    for _ in range(20):
        render_board(board)
        board = get_next_generation(board)
        time.sleep(0.3)

if __name__ == "__main__":
    main()

EMPTY = 0
WHITE_PIECE = 1
BLACK_PIECE = 2
WHITE_KING = 3
BLACK_KING = 4

#present all the information
def initialize_board():
    board = [[EMPTY for _ in range(8)] for _ in range(8)]
    
    for row in range(3):
        for col in range(8):
            if (row + col) % 2 == 1:
                board[row][col] = WHITE_PIECE
            if (row + col) % 2 == 1 and row >= 5:
                board[row + 5][col] = BLACK_PIECE

    return board

def print_board(board):
    symbols = {
        EMPTY: '.',
        WHITE_PIECE: 'w',
        BLACK_PIECE: 'b',
        WHITE_KING: 'W',
        BLACK_KING: 'B'
    }
    for row in board:
        print(" ".join(symbols[cell] for cell in row))
      
#function to move pieces and validate moves      
def is_valid_move(board, start, end):
    x1, y1 = start
    x2, y2 = end

    if board[x2][y2] != EMPTY:
        return False

    piece = board[x1][y1]
    if piece == WHITE_PIECE:
        return (x2 == x1 + 1 and abs(y2 - y1) == 1)
    elif piece == BLACK_PIECE:
        return (x2 == x1 - 1 and abs(y2 - y1) == 1)
    elif piece in (WHITE_KING, BLACK_KING):
        return abs(x2 - x1) == abs(y2 - y1)
    return False

#Capturing involves jumping over an opponent's piece. a very clever line of code which makes this concept to realization :DDD
def move_piece(board, start, end):
    if not is_valid_move(board, start, end):
        return False
    
    x1, y1 = start
    x2, y2 = end
    board[x2][y2] = board[x1][y1]
    board[x1][y1] = EMPTY
    return True

def is_valid_capture(board, start, middle, end):
    x1, y1 = start
    x2, y2 = middle
    x3, y3 = end

    if board[x3][y3] != EMPTY:
        return False

    piece = board[x1][y1]
    if piece == WHITE_PIECE and board[x2][y2] in (BLACK_PIECE, BLACK_KING):
        return (x3 == x1 + 2 and abs(y3 - y1) == 2 and x2 == x1 + 1 and abs(y2 - y1) == 1)
    elif piece == BLACK_PIECE and board[x2][y2] in (WHITE_PIECE, WHITE_KING):
        return (x3 == x1 - 2 and abs(y3 - y1) == 2 and x2 == x1 - 1 and abs(y2 - y1) == 1)
    elif piece in (WHITE_KING, BLACK_KING):
        return abs(x3 - x1) == 2 and abs(y3 - y1) == 2 and abs(x2 - x1) == 1 and abs(y2 - y1) == 1
    return False

def capture_piece(board, start, middle, end):
    if not is_valid_capture(board, start, middle, end):
        return False
    
    x1, y1 = start
    x2, y2 = middle
    x3, y3 = end
    board[x3][y3] = board[x1][y1]
    board[x1][y1] = EMPTY
    board[x2][y2] = EMPTY
    return True

#promotion
def promote_to_king(board):
    for col in range(8):
        if board[0][col] == BLACK_PIECE:
            board[0][col] = BLACK_KING
        if board[7][col] == WHITE_PIECE:
            board[7][col] = WHITE_KING

#manages the game flow
def check_winner(board):
    white_remaining = any(cell in (WHITE_PIECE, WHITE_KING) for row in board for cell in row)
    black_remaining = any(cell in (BLACK_PIECE, BLACK_KING) for row in board for cell in row)

    if not white_remaining:
        return 'Black wins!'
    if not black_remaining:
        return 'White wins!'
    return None

def game_loop():
    board = initialize_board()
    current_player = WHITE_PIECE

    while True:
        print_board(board)
        winner = check_winner(board)
        if winner:
            print(winner)
            break

        if current_player == WHITE_PIECE:
            print("White's turn")
        else:
            print("Black's turn")

        start = tuple(map(int, input("Enter the start position (x y): ").split()))
        end = tuple(map(int, input("Enter the end position (x y): ").split()))

        if move_piece(board, start, end):
            promote_to_king(board)
            current_player = BLACK_PIECE if current_player == WHITE_PIECE else WHITE_PIECE
        else:
            print("Invalid move, try again.")

if __name__ == "__main__":
    game_loop()

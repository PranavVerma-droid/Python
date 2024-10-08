print("This is a Simple Chess Project.")
print("Made by Pranav Verma, for the Finals Project.")
print("The Chess Notation is Like this: <initial_pos><final_pos>")
print("The Initial Position Is what piece you want to move, eg. e2")
print("The Final Position Is where you want to move it, eg. e4")

PIECES = {
    'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚', 'p': '♟',
    'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔', 'P': '♙',
    ' ': ' '
}

board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

def is_move_valid(start_row, start_col, end_row, end_col, player):
    piece = board[start_row][start_col]
    
    # Check if the piece belongs to the current player
    if (player == 1 and piece.islower()) or (player == 2 and piece.isupper()):
        return False
    
    # Basic movement rules for pieces
    direction = -1 if piece.isupper() else 1  # 1 for Black, -1 for White
    if piece.lower() == 'p':
        # Check for pawn movement
        if (end_col == start_col and board[end_row][end_col] == ' ' and
            ((start_row == 6 and direction == -1 and end_row == 4) or
             (start_row == 1 and direction == 1 and end_row == 3) or
             (end_row == start_row + direction))):
            return True
        # Check for pawn captures
        if (abs(end_col - start_col) == 1 and end_row == start_row + direction and
                board[end_row][end_col] != ' ' and
                board[end_row][end_col].islower() != piece.islower()):
            return True
        return False

    if piece.lower() == 'r':
        if (start_row == end_row or start_col == end_col):
            return not any(board[row][col] != ' ' for row in range(min(start_row, end_row) + 1, max(start_row, end_row))
                                                          for col in range(min(start_col, end_col) + 1, max(start_col, end_col)))
        return False

    if piece.lower() == 'n':
        return (abs(end_row - start_row), abs(end_col - start_col)) in [(2, 1), (1, 2)]

    if piece.lower() == 'b':
        if abs(end_row - start_row) == abs(end_col - start_col):
            return not any(board[start_row + i * (end_row - start_row) // abs(end_row - start_row)]
                           [start_col + i * (end_col - start_col) // abs(end_col - start_col)] != ' '
                           for i in range(1, abs(end_row - start_row)))
        return False

    if piece.lower() == 'q':
        return is_move_valid(start_row, start_col, end_row, end_col, player)  # Rook-like + Bishop-like movement

    if piece.lower() == 'k':
        return max(abs(end_row - start_row), abs(end_col - start_col)) == 1

    return False  # If the piece type is unknown or not valid

player = 1
while True:
    row_number = 8
    print(" ")
    print("Player " + str(player) + "'s turn")
    print(" ")

    for row in board:
        print(str(row_number) + "  ", end='')
        for piece in row:
            print(PIECES[piece], end=' ')
        print("  " + str(row_number))
        row_number -= 1
    print("")
    print("   a b c d e f g h")
    print(" ")
    
    move = input(f"Player {player}, enter your move (e.g., e2e4) or 'quit' to end: ")
    if move.lower() == 'quit':
        break
        
    cols = 'abcdefgh'
    start_col, start_row, end_col, end_row = cols.index(move[0]), 8 - int(move[1]), cols.index(move[2]), 8 - int(move[3])
    
    if is_move_valid(start_row, start_col, end_row, end_col, player):
        board[end_row][end_col] = board[start_row][start_col]
        board[start_row][start_col] = ' '
        player = 3 - player  # Switch player
    else:
        print("Illegal move, try again!")

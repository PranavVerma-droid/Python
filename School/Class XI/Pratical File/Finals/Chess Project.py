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
        row_number = row_number - 1
    print("")
    print("   a b c d e f g h")
    print(" ")
    
    move = input(f"Player {player}, enter your move (e.g., e2e4) or 'quit' to end: ")
    if move.lower() == 'quit':
        break
        
    cols = 'abcdefgh'
    start_col, start_row, end_col, end_row = cols.index(move[0]), 8 - int(move[1]), cols.index(move[2]), 8 - int(move[3])
    
    board[end_row][end_col] = board[start_row][start_col]
    board[start_row][start_col] = ' '
    player = 3 - player 

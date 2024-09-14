import chess
import chess.svg

# Create a new chess board
board = chess.Board()

# Print the board
print(board)

# Make a move (e.g., move the pawn from e2 to e4)
board.push_san("e4")

# Print the board again
print(board)

# Get the current state of the board in FEN notation
fen = board.fen()
print(fen)

# Undo the last move
board.pop()
print(board)

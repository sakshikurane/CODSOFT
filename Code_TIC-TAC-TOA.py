import tkinter as tk
from tkinter import messagebox
from copy import deepcopy

# Initialize global variables
player_symbol = "X"
ai_symbol = "O"
current_turn = "Player"
scores = {"Player": 0, "AI": 0, "Draws": 0}

# Colors for the joyful theme
bg_color = "#FFC300"  # Bright yellow
button_color = "#FF5733"  # Orange
text_color = "#DAF7A6"  # Light green

# Function to check for a winner
def check_winner(board, symbol):
    # Rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == symbol for j in range(3)):  # Row
            return True
        if all(board[j][i] == symbol for j in range(3)):  # Column
            return True
    # Diagonals
    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2 - i] == symbol for i in range(3)):
        return True
    return False

# Function to check for a draw
def is_draw(board):
    return all(board[i][j] != "" for i in range(3) for j in range(3))

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, ai_symbol):
        return 10 - depth
    if check_winner(board, player_symbol):
        return depth - 10
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = ai_symbol
                    score = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ""
                    best_score = max(best_score, score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = player_symbol
                    score = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ""
                    best_score = min(best_score, score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score

# AI's move
def ai_move():
    global board, current_turn
    best_score = -float("inf")
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = ai_symbol
                score = minimax(board, 0, False, -float("inf"), float("inf"))
                board[i][j] = ""
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    if best_move:
        i, j = best_move
        board[i][j] = ai_symbol
        buttons[i][j].config(text=ai_symbol, state="disabled")
        if check_winner(board, ai_symbol):
            scores["AI"] += 1
            messagebox.showinfo("Game Over", "AI wins!")
            restart_game()
        elif is_draw(board):
            scores["Draws"] += 1
            messagebox.showinfo("Game Over", "It's a draw!")
            restart_game()
        else:
            current_turn = "Player"

# Handle button click
def on_click(i, j):
    global board, current_turn
    if current_turn == "Player" and board[i][j] == "":
        board[i][j] = player_symbol
        buttons[i][j].config(text=player_symbol, state="disabled")
        if check_winner(board, player_symbol):
            scores["Player"] += 1
            messagebox.showinfo("Game Over", "You win!")
            restart_game()
        elif is_draw(board):
            scores["Draws"] += 1
            messagebox.showinfo("Game Over", "It's a draw!")
            restart_game()
        else:
            current_turn = "AI"
            ai_move()

# Restart the game
def restart_game():
    global board, current_turn
    board = [["" for _ in range(3)] for _ in range(3)]
    current_turn = "Player"
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state="normal")
    update_scores()

# Update the score display
def update_scores():
    score_label.config(text=f"Player: {scores['Player']} | AI: {scores['AI']} | Draws: {scores['Draws']}")

# Set player symbol
def set_symbol(symbol):
    global player_symbol, ai_symbol
    player_symbol = symbol
    ai_symbol = "X" if symbol == "O" else "O"
    restart_game()

# Main GUI setup
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.config(bg=bg_color)

# Add game title label at the top
title_label = tk.Label(root, text="TIC-TAC Victory", font=("Arial", 24, "bold"), fg=text_color, bg=bg_color)
title_label.grid(row=0, column=0, columnspan=3, pady=10)

# Create the board
board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

# Create buttons for the grid
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                                  bg=button_color, fg=text_color,
                                  command=lambda i=i, j=j: on_click(i, j))
        buttons[i][j].grid(row=i + 1, column=j, padx=5, pady=5)

# Create a frame for score and symbol selection
frame = tk.Frame(root, bg=bg_color)
frame.grid(row=4, column=0, columnspan=3, pady=10)

# Add score label
score_label = tk.Label(frame, text="", font=("Arial", 14), bg=bg_color, fg=text_color)
score_label.pack()

# Add symbol selection buttons
symbol_frame = tk.Frame(frame, bg=bg_color)
symbol_frame.pack(pady=10)
tk.Label(symbol_frame, text="Choose your symbol:", font=("Arial", 12), bg=bg_color, fg=text_color).grid(row=0, column=0, columnspan=2)
tk.Button(symbol_frame, text="X", font=("Arial", 12), bg=button_color, fg=text_color,
          command=lambda: set_symbol("X")).grid(row=1, column=0, padx=5)
tk.Button(symbol_frame, text="O", font=("Arial", 12), bg=button_color, fg=text_color,
          command=lambda: set_symbol("O")).grid(row=1, column=1, padx=5)

# Initialize the scores and start the game
update_scores()
restart_game()

# Run the GUI event loop
root.mainloop()


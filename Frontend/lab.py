import tkinter as tk
from tkinter import messagebox

def check_winner():
    for row in board:
        if row[0]["text"] == row[1]["text"] == row[2]["text"] != "":
            return row[0]["text"]
    for col in range(3):
        if board[0][col]["text"] == board[1][col]["text"] == board[2][col]["text"] != "":
            return board[0][col]["text"]
    if board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] != "":
        return board[0][0]["text"]
    if board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] != "":
        return board[0][2]["text"]
    return None

def on_click(row, col):
    global turn
    if board[row][col]["text"] == "" and not winner:
        board[row][col]["text"] = turn
        win = check_winner()
        if win:
            messagebox.showinfo("Game Over", f"{win} wins!")
            reset_board()
        elif all(board[r][c]["text"] != "" for r in range(3) for c in range(3)):
            messagebox.showinfo("Game Over", "It's a Draw!")
            reset_board()
        else:
            turn = "O" if turn == "X" else "X"

def reset_board():
    global turn, winner
    for r in range(3):
        for c in range(3):
            board[r][c]["text"] = ""
    turn = "X"
    winner = None

root = tk.Tk()
root.title("Tic-Tac-Toe")

turn = "X"
winner = None
board = [[None for _ in range(3)] for _ in range(3)]

for r in range(3):
    for c in range(3):
        board[r][c] = tk.Button(root, text="", font=("Arial", 20), width=5, height=2,
                                command=lambda r=r, c=c: on_click(r, c))
        board[r][c].grid(row=r, column=c)

reset_button = tk.Button(root, text="Reset", font=("Arial", 14), command=reset_board)
reset_button.grid(row=3, column=0, columnspan=3)

root.mainloop()

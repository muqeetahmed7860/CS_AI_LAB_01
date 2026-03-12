import tkinter as tk
from tkinter import messagebox

# Board
board = ["_" for i in range(9)]
current_player = "x"

# Evaluation Function
def evaluate():
    win_conditions = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]

    for a,b,c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] != "_":
            if board[a] == "x":
                return 10
            else:
                return -10
    return 0


def check_game():
    score = evaluate()

    if score == 10:
        messagebox.showinfo("Game Over","Player X Wins (+10)")
        reset()
    elif score == -10:
        messagebox.showinfo("Game Over","Player O Wins (-10)")
        reset()
    elif "_" not in board:
        messagebox.showinfo("Game Over","Draw (0)")
        reset()


def click(i):
    global current_player

    if board[i] == "_":
        board[i] = current_player
        buttons[i]["text"] = current_player

        check_game()

        if current_player == "x":
            current_player = "o"
        else:
            current_player = "x"


def reset():
    global board,current_player

    board = ["_" for i in range(9)]
    current_player = "x"

    for b in buttons:
        b["text"] = ""


# GUI
root = tk.Tk()
root.title("Tic Tac Toe")

buttons = []

for i in range(9):
    btn = tk.Button(root,text="",font=("Arial",25),width=5,height=2,
                    command=lambda i=i: click(i))
    btn.grid(row=i//3,column=i%3)
    buttons.append(btn)

root.mainloop()
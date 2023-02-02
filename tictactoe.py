# TicTacToe in Python

import numpy as np
import random

# Initializes the board as a nxn grid with all values set to "None"
def init(size):
    board = np.empty((size, size), dtype=object)
    board.fill('-')
    return board

# Renders the board onto the screen. 
def render(board):
    rows = board.shape[0]
    columns = board.shape[1]

    # Renders the top row of the board
    print("    0 1 2")
    print("   -------")

    # Renders the contents of the board
    currentRow = "0 |"
    for i in range(rows):
        for j in range(columns):
            currentRow = currentRow + " " + board[i][j]
        print(currentRow + " |")
        currentRow = str(i+1) + " |"
    
    # Renders the bottom of the board
    print("   -------")

# Returns the next state of the board after prompting the player to make a move
def next_board_state(board, player):
    width = board.shape[0]
    height = board.shape[1]

    if player == "O":
        print("Player O's turn!")
        try:
            xPos = int(input("Enter the row where you would like to place a O. "))
            yPos = int(input("Enter the column where you would like to place a O. "))
        except ValueError:
            print("\n")
            print("That wasn't a valid move. Please try again.")
            print("\n")
            render(board)
            next_board_state(board, player)

        # Boundary and collision checking 
        if inBounds(width, height, xPos, yPos):
            if board[xPos][yPos] == "-":
                board[xPos][yPos] = "O"
            else:
                print("\n")
                print("That wasn't a valid move. Please try again.")
                print("\n")
                render(board)
                next_board_state(board, player)
        else: 
            print("\n")
            print("That wasn't a valid move. Please try again.")
            print("\n")
            render(board)
            next_board_state(board, player)

    else:
        print("Player X's turn!")
        try:
            xPos = int(input("Enter the row where you would like to place an X. "))
            yPos = int(input("Enter the column where you would like to place an X. "))
        except ValueError:
            print("\n")
            print("That wasn't a valid move. Please try again.")
            print("\n")
            render(board)
            next_board_state(board, player)

        # Boundary and collision checking 
        if inBounds(width, height, xPos, yPos):
            if board[xPos][yPos] == "-":
                board[xPos][yPos] = "X"
            else:
                print("\n")
                print("That wasn't a valid move. Please try again.")
                print("\n")
                render(board)
                next_board_state(board, player)
        else: 
            print("\n")
            print("That wasn't a valid move. Please try again.")
            print("\n")
            render(board)
            next_board_state(board, player)
    
    return board

# Helper function to check if a player has won 
def winningBoard(board):
    # For each column, we want to check the vertical, horizontal and diagonals. 
    count = 3
    rows = board.shape[0]
    columns = board.shape[1]

    return False or checkHorizontals(board) or checkVerticals(board) or checkDiagonals(board)

# Helper function to check horizontals
def checkHorizontals(board):
    horizontal1 = board[0][0] != "-" and (board[0][0] == board[1][0] == board[2][0])
    horizontal2 = board[0][1] != "-" and (board[0][1] == board[1][1] == board[2][1])
    horizontal3 = board[0][2] != "-" and (board[0][2] == board[1][2] == board[2][2])
    return horizontal1 or horizontal2 or horizontal3

# Helper function to check verticals 
def checkVerticals(board):
    vertical1 = board[0][0] != "-" and (board[0][0] == board[0][1] == board[0][2])
    vertical2 = board[1][0] != "-" and (board[1][0] == board[1][1] == board[1][2])
    vertical3 = board[2][0] != "-" and (board[2][0] == board[2][1] == board[2][2])
    return vertical1 or vertical2 or vertical3

# Helper function to check diagonals 
def checkDiagonals(board):
    diagonal1 = board[0][0] != "-" and (board[0][0] == board[1][1] == board[2][2]) 
    diagonal2 = board[2][0] != "-" and (board[2][0] == board[1][1] == board[0][2])
    return diagonal1 or diagonal2


# Helper function to check if no players have won
def fullBoard(board):
    width = board.shape[0]
    height = board.shape[1]

    fullBoard = True
    for i in range(width):
        for j in range(height):
            fullBoard = fullBoard and (board[i][j] != "-")
    return fullBoard

# Helper function to determine if a certain move is allowed within the board
def inBounds(width, height, xPos, yPos):
    return (xPos >= 0 and xPos <= width-1) and (yPos >= 0 and yPos <= height-1)

# Driver code for the program
def main():
    print("Let's Play TicTacToe!")
    print("\n")
    initialBoard = init(3)
    render(initialBoard)
    print("\n")

    # determine turn order
    start = random.randint(0, 1)
    turn = ""
    if start == 0:
        print("Player O starts!")
        turn = "O"
    else:
        print("Player X starts!")
        turn = "X"

    current_board = initialBoard    
    while True:
        next_board = next_board_state(current_board, turn)
        print("\n")
        render(next_board)
        if fullBoard(next_board):
            print("\n")
            print("It's a tie!")
            break
        elif winningBoard(next_board):
            print("\n")
            print("Player " + turn + " wins!")       
            break
        else:
            current_board = next_board
            if turn == "O":
                turn = "X"
            else:
                turn = "O"
            print("\n")
main()
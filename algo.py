def defineBoard():
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]
    return board

def updateBoard(board, column, player):
    for row in range(5, -1, -1):
        if board[row][column] == 0:
            board[row][column] = player
            break
    return board

def printBoard(board):
    for row in board:
        print(row)

def checkWin(board, player):
    # Check horizontal
    for row in range(6):
        for col in range(4):
            if board[row][col] == player and board[row][col+1] == player and board[row][col+2] == player and board[row][col+3] == player:
                return True

    # Check vertical
    for row in range(3):
        for col in range(7):
            if board[row][col] == player and board[row+1][col] == player and board[row+2][col] == player and board[row+3][col] == player:
                return True

    # Check positive diagonal
    for row in range(3):
        for col in range(4):
            if board[row][col] == player and board[row+1][col+1] == player and board[row+2][col+2] == player and board[row+3][col+3] == player:
                return True

    # Check negative diagonal
    for row in range(3):
        for col in range(4, 7):
            if board[row][col] == player and board[row+1][col-1] == player and board[row+2][col-2] == player and board[row+3][col-3] == player:
                return True

    return False

def minimax(board, depth, isMaximizing):
    if checkWin(board, 2):
        return 10000
    elif checkWin(board, 1):
        return -10000
    elif depth == 4:
        return 0

    if isMaximizing:
        bestScore = -10000
        for column in range(7):
            if board[0][column] == 0:
                row = 0
                while row < 6 and board[row][column] == 0:
                    row += 1
                row -= 1
                board[row][column] = 2
                score = minimax(board, depth+1, False)
                board[row][column] = 0
                bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = 10000
        for column in range(7):
            if board[0][column] == 0:
                row = 0
                while row < 6 and board[row][column] == 0:
                    row += 1
                row -= 1
                board[row][column] = 1
                score = minimax(board, depth+1, True)
                board[row][column] = 0
                bestScore = min(score, bestScore)
        return bestScore

def calculateBestMove(board):
    bestScore = -10000
    bestColumn = 0
    for column in range(7):
        if board[0][column] == 0:
            row = 0
            while row < 6 and board[row][column] == 0:
                row += 1
            row -= 1
            board[row][column] = 2
            score = minimax(board, 0, False)
            board[row][column] = 0
            if score > bestScore:
                bestScore = score
                bestColumn = column
    return bestColumn

def checkValidMove(board, column):
    if board[0][column] == 0 and column >= 0 and column <= 6:
        return True
    else:
        return False
    
# def mainPvP(turn):
#     if turn == 1:
#         print("Player 1's turn")
#         chosenColumn = int(input("Enter a column: "))
#         if checkWin(board, 1):
#             print("Player 1 wins!")
#             return
#         else:
#             turn = 2
#             printBoard(updateBoard(board, chosenColumn, 1))
#             main(turn)
#     elif turn == 2:
#         print("Player 2's turn")
#         chosenColumn = int(input("Enter a column: "))
#         if checkWin(board, 2):
#             print("Player 2 wins!")
#             return
#         else:
#             turn = 1
#             printBoard(updateBoard(board, chosenColumn, 2))
#             main(turn)
#     else:
#         return

def main(turn):
    if turn == 1:
        print("Player 1's turn")
        chosenColumn = int(input("Enter a column: "))
        if checkValidMove(board, chosenColumn) == False:
            print("Invalid column")
            main(turn)
        else:
            if checkWin(board, 1):
                print("Player 1 wins!")
                return
            else:
                turn = 2
                printBoard(updateBoard(board, chosenColumn, 1))
                main(turn)
    elif turn == 2:
        print("Player 2's turn")
        chosenColumn = calculateBestMove(board)
        if checkWin(board, 2):
            print("Player 2 wins!")
            return
        else:
            turn = 1
            printBoard(updateBoard(board, chosenColumn, 2))
            main(turn)
    else:
        return


global board
global turn

turn = 1
board = defineBoard()
main(turn)
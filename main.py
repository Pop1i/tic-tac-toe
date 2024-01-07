board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def printBoard():
    print("\n  1 2 3")
    rowIndex = 0
    for row in board:
        rowIndex+=1
        print(end=f"{rowIndex} ")
        for piece in row: print(end=f"{piece} ")
        print()

def putPiece(piece: str, pos: tuple) -> bool:
    global board
    if board[pos[0]][pos[1]] == " ":
        board[pos[0]][pos[1]] = piece
        return True
    else:
        return False
    
def isWon() -> bool:
    won: bool = False
    for piece in "x","o":
        if board[0][0] == piece and board[1][1] == piece and board[2][2] == piece: won = True
        if board[0][2] == piece and board[1][1] == piece and board[2][0] == piece: won = True
        for i in range(3):
            if board[i][:] == [piece,piece,piece]: won = True
            if board[0][i] == piece and board[1][i] == piece and board[2][i] == piece: won = True
    return won

if __name__ == "__main__":
    turn = "x"
    while True:
        printBoard()
        print(f"\n{turn}'s turn")

        cords = input("yx:")
        if len(cords) == 2: cords = (int(cords[0])-1,int(cords[1])-1)
        else: print("\nerror"), exit(1)

        putPiece(turn, cords)

        if isWon(): printBoard(), print(f"\n{turn} won"), exit(0)

        if turn =="x": turn = "o"
        else: turn = "x"

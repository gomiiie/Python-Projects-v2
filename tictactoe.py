import random

gameRun = True
opponent = 0
priority = ""
p1char, p2char = 9

grid=[["9"]*3]*3

winningBoards = {0: [1, 3, 4],
                 }

moveList = [[],[]]

def coordinateToInt(X, Y):
    return (3*int(X)) + int(Y)

def printGrid(grid):
    for row in grid:
        print("|", end = " ")
        for ele in row:
            if ele == 0:
                char = "X"
            elif ele == 1:
                char = "O"
            else:
                char = " " 
            print(char, end = " | ")
        print("\n")

def player1Move(p1char, grid, moveList):
    choiceX, choiceY = input("Player 1's turn: ").split()
    while grid[choiceX][choiceY] != 9:
        choiceX, choiceY = input("Slot taken. Try another: ").split()
    grid[choiceX][choiceY] = p1char
    moveList[0].append(coordinateToInt(choiceX,choiceY))

def player2Move(type, p2char, grid, moveList):

    if type == 1:
        choiceX, choiceY  = random.randint(0,2), random.randint(0,2)
        while grid[choiceY][choiceX] != 9:
            choiceX, choiceY  = random.randint(0,2), random.randint(0,2)  
        print("Player 2's turn: {choiceX} {choiceY}")

    else:
        choice = input("Player 2's turn: ").split()
        while grid[choice[0]][choice[1]] != 9:
            choiceX, choiceY = input("Slot taken. Try another: ").split()
    
    grid[choiceX][choiceY] = p2char
    moveList[1].append(coordinateToInt(choiceX, choiceY))



print("="*25 + "TIC-TAC-TOE" + "="*25)

opponent = input("Would you like to play against another player or the computer? \n" \
                 "Enter 1 for CPU, 2 for human player, 3 to exit: ")
opponent = int(opponent)
if opponent == 3:
    gameRun = False


priority = input("Choose O/X for player 1: ").upper()
while 1:
    if priority == "X":
        p1char = 0
        p2char = 1
        break
    elif priority == "0":
        p1char = 1
        p2char = 0
        break
    else: 
        priority = input("Invalid input. Only O/X: ")

print("BEGIN!")
print("All inputs must be coordinates from 0 to 2, separated by a space")

printGrid(grid)

while gameRun:
    if priority == "X":
        player1Move(p1char, grid, moveList)
        player2Move(opponent, p2char, grid, moveList)

    elif priority == "O":
        player2Move(opponent, p2char, grid, moveList)
        player1Move(p1char, grid, moveList)
    
    printGrid()
    gameRun, winner = winCheck()
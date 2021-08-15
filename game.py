board = [["|"," ","|"," ","|"," ","|" ],
         ["|"," ","|"," ","|"," ","|" ],
         ["|"," ","|"," ","|"," ","|" ]]
def countSpaces():
    res = 0
    for i in range(len(board)):
        res += board[i].count(" ")
    return res   
def boardPrint():
    print(*board[0], sep = "")
    print(*board[1], sep = "")
    print(*board[2], sep = "")

def placeTile(num, player):
    # There is probably a better way to do this
    if num >= 1 and num <= 3:
        r = 0
        x = (num-1)*2+1
    elif num >= 4 and num <= 6:
        r = 1
        x = (num-4)*2+1
    elif num >= 7 and num <= 9:
        r = 2
        x = (num-7)*2+1
    else:
        return 0
    if board[r][x] == "o" or board[r][x] == 'x':
            print("tile already taken!: ")
            placeTile(int(input("Player Choose a number between 1 and 9 to place your tile: ")), player)
    else:
        if player == 1:
            board[r][x]= "x"
        else:
            board[r][x] = "o"

def isWon():
    #horizontal line win
    for i in range(len(board)):
        if board[i].count('x') == 3 or board[i].count('o') == 3:
            return True
    #verticle win
        if board[0][1]+board[1][1]+board[2][1] == "xxx" or board[0][1]+board[1][1]+board[2][1] == "ooo":
            return True
        if board[0][3]+board[1][3]+board[2][3] == "xxx" or board[0][3]+board[1][3]+board[2][3] == "ooo":
            return True
        if board[0][5]+board[1][5]+board[2][5] == "xxx" or board[0][5]+board[1][5]+board[2][5] == "ooo":
            return True
    #diagonal win
        if board[0][1] + board[1][3] + board[2][5] == "xxx" or board[0][1] + board[1][3] + board[2][5] == "ooo":
            return True
        if board[2][1] + board[1][3] + board[0][5] == "xxx" or board[2][1] + board[1][3] + board[0][5] == "ooo":
            return True
    return False
p1_turn = True
while countSpaces() != 0:
    if p1_turn:
        player = 1
    else:
        player = 2
    boardPrint()
    num = int(input("Player Choose a number between 1 and 9 to place your tile: "))
    placeTile(num,player)
    if isWon():
        print("Player "+str(player)+" won!")
        break
    p1_turn = not p1_turn    
boardPrint()
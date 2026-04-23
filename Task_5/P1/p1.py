import random
mode_player = True
draw_mode = True
player1=''
player2=''
move_num = 0
matrix = [
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
]
pos_map ={
    1:(0,0), 2:(0,1), 3:(0,2),
    4:(1,0), 5:(1,1), 6:(1,2),
    7:(2,0), 8:(2,1), 9:(2,2)
}
def print_borad():
    print("\n")
    for i in range(0,3):
        print(f" {matrix[i][0]} | {matrix[i][1]} | {matrix[i][2]} ",end="\n")
        if(i<2):
            print("-----------",end="\n")
    print("\n")

def play():
    global player1,player2,mode_player,move_num,draw_mode
    while(move_num< 9):
        if(move_num % 2 == 0):
            try:
                pos = int(input("player1, choose between(1-9):"))
                if(pos < 1 or pos > 9):
                    continue
            except ValueError:
                print("Please enter a valid number!")
                continue
            update_matrix(pos,player1)
            if(mode_player):
                print_borad()
            if(check_winner()):
                if(not mode_player):
                   print_borad()
                print("Congratulations player1 you won !!!!!!")
                draw_mode = False
                break;
        else:
            if(mode_player):
                try:
                    pos = int(input("player2, choose between(1-9):"))
                    if(pos < 1 or pos > 9):
                        print("invalid input, please try again")
                        continue 
                except ValueError:
                    print("Please enter a valid number!")
                    continue           
            else:
                pos = random.randint(1, 9)
                while(check_found(pos)):
                    pos = random.randint(1, 9)
            update_matrix(pos,player2)
            print_borad()
            if(check_winner()):
                if(mode_player):
                    print("Congratulations player2 you won !!!!!!")
                else:
                    print("Sorry you lost !!!!!!")
                draw_mode = False
                break;
    if(draw_mode):
        print("\noh!!! It's draw")

def check_winner():
    for i in range(0,3):
        if(matrix[i][0] == matrix[i][1] == matrix[i][2] != ' '):
            return True
        elif(matrix[0][i] == matrix[1][i] == matrix[2][i] != ' '):
            return True
        
    if matrix[0][0] == matrix[1][1] == matrix[2][2] != ' ':
        return True
    if matrix[0][2] == matrix[1][1] == matrix[2][0] != ' ':
        return True 
    
    return False   

def ask_user():
    global player1,player2,mode_player
    player1= input("Choose your symbol 'X or O' : ").upper()
    if(player1 == 'X'):
        player2 = 'O'
    elif(player1 == 'O'):
        player2 = 'X'
    else:
        print("wrong input, choose again")
        return ask_user()

    type = input("Choose 'P' to play with a player or 'C' to play with computer: ").upper()
    if(type == 'P'):
        mode_player = True
    elif(type == 'C'):
        mode_player = False
    else:
        print("wrong input, choose again\nstart again")
        return ask_user()
    play()

def update_matrix(pos,symbol):
    global mode_player,move_num
    while((check_found(pos))):
        print("filled position")
        try:
            pos = int(input("choose between(1-9):"))
        except ValueError:
            print("Invalid input, enter a number.")
            continue
        
    row,col = pos_map[pos]
    matrix[row][col] = symbol
    move_num += 1

def check_found(pos):
    row, col = pos_map[pos] 
    if (matrix[row][col] != ' '):
        return True
    else:
        return False

ask_user()


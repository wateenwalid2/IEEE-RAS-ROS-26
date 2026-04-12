def move_player(xy_coor,dir):
    x,y = xy_coor
    if(dir == "up"):
        y+= 1
    elif (dir == "down"):
        y-= 1
    elif (dir == "right"):
        x+= 1
    elif (dir == "left"):
        x-= 1

    return (x,y)

print(move_player((5,4),"left"))




    
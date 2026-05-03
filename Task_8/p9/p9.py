counter=0
n= int(input())
if((n>=1) and (n<= 100)):
    for i in range(n):
        inp = input().split()
        ls = [int(inp[0]),int(inp[1])]
        if((ls[0] >= 0) and (ls[0] <= ls[1]) and (ls[1] <= 100)):
            if((ls[0] < ls[1]) and ((ls[1] - ls[0]) >= 2)):
                counter +=1
        else:
            print("wrong range")
            break
    
    print(counter)
else:
    print("wrong range")

counter =0
n= int(input())
if((n>= 1) and (n<= 1000)):
    for i in range(n):
        inp = input().split()
        ls = [int(inp[0]),int(inp[1]),int(inp[2])]
        if(sum(ls) >= 2):
            counter +=1
    print(counter)
else:
    print("wrong range")

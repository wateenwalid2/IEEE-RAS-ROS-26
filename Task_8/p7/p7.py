total_list =[]
total_list.append(0)
n= int(input())
if((n>= 2) and (n<= 1000)):
    remain = 0
    for i in range(n):
        inp = input().split()
        ls = [int(inp[0]),int(inp[1])]
        if((ls[0] >= 0) and (ls[1] >= 0) and (ls[0] <= 1000) and (ls[1] <= 1000)):
            remain = total_list[i] - ls[0]
            total_list.append(remain + ls[1])
        else:
            print("wrong range")
            break
    
    print(max(total_list))
else:
    print("wrong range")

    

            
        

    

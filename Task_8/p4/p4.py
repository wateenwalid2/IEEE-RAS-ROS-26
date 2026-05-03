ls=[]
t= int(input())
if((t>= 1) and (t<= 9261)):
    for i in range(t):
        inp = input().split()
        if((int(inp[0]) >=0) and (int(inp[2]) <= 20) and (int(inp[1]) >=0) and (int(inp[1]) <= 20) and
                                                                (int(inp[2]) >=0) and (int(inp[2]) <= 20)):
            if((int(inp[0]) == (int(inp[1]) + int(inp[2])))):
                ls.append("YES")
            elif((int(inp[1]) == (int(inp[0]) + int(inp[2])))):
                ls.append("YES")
            elif((int(inp[2]) == (int(inp[0]) + int(inp[1])))):
                ls.append("YES")
            else:
                ls.append("NO")
        else:
            print("wrong range")
            break
    
    for result in ls:
        print(result)
else:
    print("wrong range")






        

    


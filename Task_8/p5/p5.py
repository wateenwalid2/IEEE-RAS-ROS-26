ls =[]
t= int(input())
if( (t>= 1) and (t<= 10000)):
    for i in range(t):
        inp = int(input())
        if((inp>= -5000) and (inp<= 5000)):
            if(inp >= 1900):
                ls.append("Division 1")
            elif((inp>= 1600) and (inp<= 1899)):
                ls.append("Division 2")
            elif((inp>= 1400) and (inp<= 1599)):
                ls.append("Division 3")
            elif(inp<= 1399):
                ls.append("Division 4")
        else:
            print("wrong range")
            break
    
    for result in ls:
        print(result)
else:
    print("wrong range")


            

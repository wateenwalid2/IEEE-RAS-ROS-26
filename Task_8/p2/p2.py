found_index = None
ls=[]
t = int(input())
if ((t >= 1) and (t<=100)):
    for i in range(t):
        n= int(input())
        if((n >= 3) and (n<=100)):
            inp = input().split()
            if((int(inp[0]) >= 1) and (int(inp[0])<=100)):
                first = int(inp[0])
                for j in range(1,n):
                    num = int(inp[j])
                    if((num >= 1) and (num<=100)):
                        if((first != num) and(j == 1) and (num == int(inp[j+1]))):
                            found_index = j
                            break
                        elif(first != num):
                            found_index = j+1
                            break
                        else:
                            first = num
                    else:
                        print("wrong range")
                        break
                ls.append(found_index)
            else:
                print("wrong range")
                break
        else:
            print("wrong range")
            break
    
    for result in ls:
            print(result)
else:
    print("wrong range")

                

                








            
                
                

            


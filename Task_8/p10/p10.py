ls=[]
inp = input()
if((len(inp)>=1) and (len(inp)<=200) ):
    i=0
    while (i< len(inp)):
        if(inp[i] == '.'):
            ls.append(0)
            i +=1
        else:
            if(inp[i+1] == '.'):
                ls.append(1)
            else:
                ls.append(2)
            i +=2
    for result in ls:
        print(int(result),end= "")
else:
    print("wrong range")


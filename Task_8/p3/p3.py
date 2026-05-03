ls=[]
n= int(input())
if( (n>=1) and (n<=100)):
    for i in range(n):
        inp = input()
        if(len(inp) > 10):
            ls.append(f"{inp[0]}{len(inp) - 2}{inp[len(inp) -1]}")
        else:
            ls.append(inp)
    
    for result in ls:
        print(result)
else:
    print("wrong range")
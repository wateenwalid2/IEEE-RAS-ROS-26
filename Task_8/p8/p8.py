ls =[]

t= int(input())
if((t>=1) and (t<= 10000)):
    for i in range(t):
        counter = 0
        n= int(input())
        if((n>=1) and (n<= 50)):
            inp = input().split()
            arr = list(map(int, inp))
            ls.append(max(arr)- min(arr))
        else:
            print("wrong range")
            break

    for result in ls:
        print(result)
else:
    print("wrong range")       

                
            
            

                
        

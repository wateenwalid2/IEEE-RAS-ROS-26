store = []
counter =0
q = int(input())
if((q>=1) and (q<= 1000)):
    for i in range(q):
        n= int(input())
        if((n>=1) and (n<= 20)):
            counter = 0
            read = input().split()
            s= read[0]
            t= read[1]
            t_list = list(t)
            if(len(s) == len(t)):
                for j in range(len(s)):
                    for h in range(len(t_list)):
                        if(s[j] == t_list[h]):
                            counter +=1
                            t_list.pop(h)
                            break
                if(counter == n):
                    store.append("Yes")
                else:
                    store.append("No")
            else:
                store.append("No")
        else:
            print("wrong range")
            break
    if store:
        for result in store:
            print(result)  
else:
    print("wrong range")








 



        






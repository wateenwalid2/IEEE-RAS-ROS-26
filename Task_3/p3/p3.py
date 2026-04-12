def get_common(s1,s2):
    s3 = set()
    for i in s1:
        for j in s2:
            if(i == j):
                s3.add(i)
                break
    
    return s3

s1 ={1,4,6,7,85,54}
s2 ={3,7,4,3,2,85,1,3,2}
print(get_common(s1,s2))

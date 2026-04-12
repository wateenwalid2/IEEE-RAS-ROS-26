def analyze_grades(l):
    a = {"average" : 0,"highest" : 0, "lowest" : 0}
    avg = sum(l)/len(l)
    high = max(l)
    low = min(l)
    a["average"] = avg
    a["highest"] = high
    a["lowest"] = low
    return a

ls = [50,30,25,37,90,43,55,150,100,125]
print(analyze_grades(ls))
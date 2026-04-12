import random
def get_unique_lottery():
    s = set()
    while(len(s) < 6):
        rd = random.randint(1,50)
        s.add(rd)
    return s


print(get_unique_lottery())
            



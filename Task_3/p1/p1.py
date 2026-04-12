import random
def pick_winner(l):
    if l:
        st = random.choice(l)
        return f"Congratulations for our winner \" {st} \""
    else:
        return f"No winner Today"

l1 = ["hend","jana","mohamed","khaled"]
print(pick_winner(l1))

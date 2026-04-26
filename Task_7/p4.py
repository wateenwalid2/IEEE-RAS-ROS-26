class Player:
    def __init__(self,name,score):
        self.name = name
        self.score = score

class Team:
    def __init__(self):
        self.members = []
    def add_player(self,player_obj):
        self.members.append(player_obj)
    def players_info(self):
        for p in self.members:
            print(f"Name : {p.name}, Score : {p.score}")

p1 = Player("Ahmed",30)
p2 = Player("Ibraheem",50)
t1 = Team()
t1.add_player(p1)
t1.add_player(p2)
print("The players_info in team t1 is : ")
t1.players_info()
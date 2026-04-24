class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print(f"Woof! My name is {self.name}")

d1 = Dog("wolf","German Shepherd")
print(d1.breed)
d1.bark()
class Animal:
    def speak(self):
        print("My voice")
    
class Dog(Animal):
    def speak(self):
        print("Woof")

a = Animal()
a.speak()
d = Dog()
d.speak()




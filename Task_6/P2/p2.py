class Calculator:
    def add(self,a,b):
        return a + b
    def subtract(self,a,b):
        return a - b
    def multiply(self,a,b):
        return a * b
    
calc = Calculator()
print(calc.add(5,7))
print(calc.subtract(6,3))
print(calc.multiply(4,5))
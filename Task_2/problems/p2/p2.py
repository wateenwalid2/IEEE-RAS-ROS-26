num = int(input("Enter a positive number: "))
sum = 0
even_numbers = []
if num > 0 :
    for i in range(1,num+1):
        if(i % 2 == 0):
            sum+= i
            even_numbers.append(i)

print(f"Total sum of even numbers from 1 to {num} is {sum} ({' + '.join(map(str, even_numbers))})") 


numbers = input("Enter numbers separated by space (use -1 to stop): ").split()
numbers = [int(num) for num in numbers if int(num) != -1]
if numbers:
    print(max(numbers), min(numbers))
else:
    print("No numbers entered!")
def save_divide():
    try:
        ip = input("Please enter 2 numbers: ")
        div = ip.split()
        x = float(div[0])
        y = float(div[1])
        print(f"Your result is {x/y}")

    except ZeroDivisionError:
        print("Invalid input(can't divide by zero)")
    
    except ValueError:
        print("Invalid input(can't divide Strings)")

save_divide()

    

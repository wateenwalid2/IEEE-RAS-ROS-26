def calculate_bill(price, items):
    total = 0
    for item in items:
        if item in price:
            total += price[item]
    return total



price = {"apple": 10, "banana": 30, "orange": 20}
items = ["apple", "banana", "apple","orange", "orange"]

result = calculate_bill(price, items)
print(f"Total Bill: {result}")
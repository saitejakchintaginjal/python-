day = input("Enter the day: ").lower()
age = int(input("Enter the age: "))
price = 12 if age >= 18 else 8

if day == "wednesday":
    print(price - 2)
else:
    print(price)

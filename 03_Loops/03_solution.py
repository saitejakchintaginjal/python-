# Multiplication Table Printer

number = int(input("enter the number : "))

# for i in range(1, 11):
#     if i != 5:
#         print(number * i)


for i in range(1, 11):
    if i == 5:
        continue
    print(number * i)

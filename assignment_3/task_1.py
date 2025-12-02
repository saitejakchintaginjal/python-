def fact_rec(num):
    if num == 1:
        return 1
    else:
        return num * fact_rec(num - 1)


number = int(input("Enter the number: "))
result = fact_rec(number)

print(f"factorial of {number} is {result}")

# Sum of Even numbers 

number = int(input("Enter the number : "))
sum_even_number = 0

for n in range(1, number + 1):
    if n % 2 == 0:
        sum_even_number += n
print(sum_even_number)

first = input("Give me the first number: ")

second = input("Give me the second number: ")

try:
    num1 = float(first)
    num2 = float(second)
except ValueError:
    print("Error: Please enter valid numbers.")
    exit(1)

print("Thank you!")

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")

if num2 != 0:
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("Division by zero is not allowed.")

print(f"{num1} * {num2} = {num1 * num2}")

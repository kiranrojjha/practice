# # Sum of all elements in a list (user input + for loop)

# # Ask how many numbers to enter
# n = int(input("Enter how many numbers you want in the list: "))

# # Create an empty list
# numbers = []

# # Take input from user
# for i in range(n):
#     num = float(input(f"Enter number {i + 1}: "))
#     numbers.append(num)

# # Initialize sum
# total = 0

# # Add each number using a for loop
# for num in numbers:
#     total += num

# # Display the result
# print("Your list:", numbers)
# print("Sum of all elements =", total)

# # 5 Count vowels in a string
# s = input("Enter a string: ")
# vowels = set("aeiouAEIOU")
# count = 0
# for ch in s:
#     if ch in vowels:
#         count += 1
# print("Number of vowels:", count)

# # 7 Print all keys and values from a dictionary using a for loop
# # Example dictionary (you can replace with any)
# d = {"name": "Alice", "age": 20, "branch": "CSE"}
# for key in d:
#     print("Key:", key, "Value:", d[key])

# # or using items()
# for key, value in d.items():
#     print(key, "->", value)

# # 9 Keep asking user for a number until they enter a negative number
# while True:
#     n = float(input("Enter a number (negative to stop): "))
#     if n < 0:
#         print("Negative number entered. Stopping.")
#         break
#     print("You entered:", n)

# # 10 Loop 1 to 10 but do nothing when the number is 5
# for i in range(1, 11):
#     if i == 5:
#         pass  # do nothing for 5
#     print(i)
# # Program to take dictionary input from the user and print keys and values

# # Create an empty dictionary
# student = {}

# # Ask how many key-value pairs user wants to enter
# n = int(input("Enter how many details you want to add: "))

# # Loop to get key-value pairs
# for i in range(n):
#     key = input(f"Enter key {i + 1}: ")
#     value = input(f"Enter value for '{key}': ")
#     student[key] = value   # add pair to dictionary

# # Display all keys and values
# print("\nDictionary contents:")
# for k, v in student.items():
#     print(k, "->", v)
# # star pattern 
# rows = int(input("Enter number of rows: "))
# for i in range(1, rows + 1):
#     print("*" * i)

# # Program to check if a number is prime (simpler version)

# n = int(input("Enter a number: "))

# # Prime numbers are greater than 1
# if n <= 1:
#     print("Not a prime number")
# else:
#     is_prime = True  # assume it is prime

#     # Check divisibility from 2 to n-1
#     for i in range(2, n):
#         if n % i == 0:
#             is_prime = False
#             break  # stop the loop if divisible

#     # Print result based on flag
#     if is_prime:
#         print(n, "is a prime number")
#     else:
#         print(n, "is not a prime number")

# # simple calculator:
# print("Simple Calculator. Type 'exit' as operator to quit.")

# while True:
#     num1 = input("Enter number 1: ")
#     if num1.lower() == 'exit':
#         print("Exiting calculator.")
#         break
#     num2 = input("Enter number 2: ")
#     if num2.lower() == 'exit':
#         print("Exiting calculator.")
#         break
#     op = input("Enter operator (+, -, *, /): ")
#     if op.lower() == 'exit':
#         print("Exiting calculator.")
#         break

#     num1 = float(num1)
#     num2 = float(num2)

#     if op == '+':
#         print(f"{num1} + {num2} = {num1 + num2}")
#     elif op == '-':
#         print(f"{num1} - {num2} = {num1 - num2}")
#     elif op == '*':
#         print(f"{num1} * {num2} = {num1 * num2}")
#     elif op == '/':
#         if num2 != 0:
#             print(f"{num1} / {num2} = {num1 / num2}")
#         else:
#             print("Error: Division by zero")
#     else:
#         print("Invalid operator")
    
#     print()  # blank line for readability

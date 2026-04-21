# 1
# for loop
# x=int(input("Enter the number"))
# for i in range(1,11):
      
#   print(x, "x", i, "=", x * i)
#   print(f"{x} x {i} = {x*i}")    # other way of doing

# while
# x=int(input("enter the number"))
# i=1
# while(i<11):
#     print(f"{x} x {i} = {x*i}")
#     i+=1


# 2
# l=["kiran","soham","satyam","suyash","sita","priyansha","kittu","ammu","kartikeya"]
# for name in l:
#     if(name.startswith("s")):
#         print(f"hello {name}")


# 3
# wrong
# n=int(input("enter the number till where prime no. is to be checked"))
# for i in range(2,n):
#     if(n%i)==0:
#         count=1
#         if(count==2):
#             print(i)

# # correct
# n = int(input("Enter the number till where prime numbers are to be checked: "))

# for num in range(2, n+1):   # loop through numbers from 2 to n
#     count = 0
#     for i in range(1, num+1):   # check divisibility
#         if num % i == 0:
#             count += 1
#     if count == 2:   # prime numbers have exactly 2 divisors
#         print(num)

# # or the other way is:
n = int(input("Enter the number : "))
for i in range (2,n):
    if(n%i) == 0:
        print("number is not prime")
        break
else:
    print("number is prime ") 

# 4 sum of all numbers
# n=int(input("enter the no"))
# i=1
# sum=0
# while(i<=n):
#     sum += i
#     i+=1

# print(sum)

# 5 factorial

# n=int(input("enter the number"))
# product=1
# for i in range(1,n+1):
#     product = product*i
# print(f"the factorial of {n} is {product}")

# 6 pyramid
'''
n=5
    *
   ***
  *****
 *******
*********
'''
# n = int(input("Enter the number: "))

# for i in range(1, n+1):
#     print(" " * (n-i), end="")         # print spaces
#     print("*" * (2*i-1), end="")       # print stars
#     print("")                          # new line

# n = int(input("Enter the number: "))

# for i in range(n, 0, -1):              # loop from n down to 1
#     print(" " * (n - i), end="")       # spaces increase
#     print("*" * (2*i - 1), end="")     # stars decrease
#     print("")

# table in reverse
# n = int(input("Enter the number: "))
# for i in range (10,0,-1):
#     print(f"{n} * {i} = {n*i}")

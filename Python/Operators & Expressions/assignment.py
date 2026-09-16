print("remainder of two numbers")
a=int(input("Enter a first Number:"))
b=int(input("Enter a Second Number:"))

reminder=a%b
print(f"remainder of two numbers is{reminder}")
print("-----------------------------------------")
print("number is even or odd")
num=int(input("Enter a Number:"))
if num % 2==0:
  print("Even")
else :
  print("odd")
print("---------------------------------------------")
print("Compare two numbers and print the larger one")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Larger number:", a)
else:
    print("Larger number:", b)
print("---------------------------------------------")
print("Calculate square and cube of a number")
num=int(input("Enter a Number:"))
square=num**2
cube=num**3
print("square :",square)
print("cube:",cube)
print("---------------------------------------------")
print("Check if two entered numbers are equal")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a == b:
    print("Both numbers are equal")
else:
    print("Numbers are not equal")
print("---------------------------------------------")
print("True if both numbers are positive, otherwise False")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = a > 0 and b > 0

print(result)
print("---------------------------------------------")
print("float to Intiger")
num = float(input("Enter a float number: "))
integer_num = int(num)
print("Integer:", integer_num)
print("---------------------------------------------")
print("Take a number as string, convert to int, and multiply by 10")
num = input("Enter a number: ")
num = int(num)
result = num * 10
print(result)
print("---------------------------------------------")
print("Use and & or operators to check multiple conditions")
age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))
if age >= 18 and marks >= 50:
    print("Condition 1 is True")
elif age >= 18 or marks >= 50:
    print("Condition 2 is True")
else:
    print("Both conditions are False")
print("---------------------------------------------")
print("Divide two numbers and print quotient and remainder separately")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
quotient = a // b
remainder = a % b
print("Quotient:", quotient)
print("Remainder:", remainder)
print('name:kunal patel,age:21,city:valsad')
print("----------------------------------")
print("Sum of two number")
a=int(input("Enter First  Number:"))
b=int(input("Enter Second Number:"))
c=a+b
print(f"Sum Of Two Number is:{c}")
print("----------------------------------")
print("Celsius to Fahrenheit Convert")
d=float(input("Enter a Temperature in Celsius: "))
F = ( d * 9/5) + 32
print(f"Your Temperature in Fahrenheit is :{F} °F")
print("----------------------------------")
print("Convert name into Upper case")
name = input("Enter your name: ")
print(name.upper())
print("----------------------------------")
print("User age find")
birth_year = int(input("Enter your birth year: "))
current_year = 2026
age = current_year - birth_year
print("Your age is:", age)
print("----------------------------------")
print("swap two number")
g= int(input("Enter first number: "))
h = int(input("Enter second number: "))
g, h = h, g
print("After swapping:")
print("g =", g)
print("h =", h)
print("----------------------------------")
print("Find Area of rectangle")
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
print("Area of rectangle =", area)
print("----------------------------------")
print("find number is positive or not ")
num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
  
print("----------------------------------")
print("find average of two number ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
average = (num1 + num2) / 2
print("Average =", average)




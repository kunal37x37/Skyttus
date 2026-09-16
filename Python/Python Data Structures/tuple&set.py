print("------------------------------------");
print("Create a tuple with 5 numbers")
numbers = (10, 20, 30, 40, 50)
print(numbers)
print("------------------------------------");
print("Access the third element in a tuple")
numbers = (10, 20, 30, 40, 50)
print(numbers[2])
print("------------------------------------");
print("Unpack a tuple into separate variables")
numbers = (10, 20, 30)
a, b, c = numbers
print(a)
print(b)
print(c)
print("------------------------------------");
print("Create a set of 5 fruits")
fruits = {"apple", "banana", "mango", "orange", "grapes"}
print(fruits)
print("------------------------------------");
print("Add a new fruit to the set")
fruits = {"apple", "banana", "mango", "orange", "grapes"}
fruits.add("watermelon")
print(fruits)
print("------------------------------------");
print("Remove an element from a set")
fruits = {"apple", "banana", "mango", "orange"}
fruits.remove("banana")
print(fruits)
print("------------------------------------");
print("Find union of two sets")
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.union(set2)
print(result)
print("------------------------------------");
print("Find intersection of two sets")
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result = set1.intersection(set2)
print(result)
print("------------------------------------");
print("Check if one set is subset of another")
set1 = {1, 2}
set2 = {1, 2, 3, 4}
if set1.issubset(set2):
    print("set1 is a subset of set2")
else:
    print("set1 is not a subset of set2")
print("------------------------------------");
print(" Remove duplicate values using a set")
numbers = [1, 2, 2, 3, 4, 4, 5, 5]
unique_numbers = set(numbers)
print(unique_numbers)

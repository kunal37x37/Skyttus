print("------------------START----------------------")
print("Create a list")
movies = ["Avengers", "Avatar", "Titanic", "Inception", "Interstellar"]
print(movies)
print("------------------------------------------------")
print("Add a new movies")
movies = ["Avengers", "Avatar", "Titanic", "Inception", "Interstellar"]
new_movie = input("Enter new movie: ")
movies.append(new_movie)
print(movies)
print("------------------------------------------------")
print("Remove the first movie")
movies = ["Avengers", "Avatar", "Titanic", "Inception", "Interstellar"]
movies.pop(0)
print(movies)
print("------------------------------------------------")
print("Sort numbers in ascending order")
numbers = [50, 10, 30, 20, 40]
numbers.sort()
print(numbers)
print("------------------------------------------------")
print("Reverse a list")
numbers = [10, 20, 30, 40, 50]
numbers.reverse()
print(numbers)
print("------------------------------------------------")
print("Find the largest number")
numbers = [10, 50, 20, 90, 30]
print("Largest:", max(numbers))
print("------------------------------------------------")
print("Merge two list")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged = list1 + list2
print(merged)
print("------------------------------------------------")
print("Access last element without using index number")
numbers = [10, 20, 30, 40, 50]
last = numbers.pop()
print("Last element:", last)
print("-------------------------------------------------")
print("Create nested list and access specific inner element")
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(numbers[1][2])
print("--------------------------------------------------")
print("Count how many times an element appears")
numbers = [10, 20, 10, 30, 10, 40]
count = numbers.count(10)
print("10 appears", count, "times")
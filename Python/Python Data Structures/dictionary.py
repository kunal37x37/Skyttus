print("------------------------------------------------")
print("Create dictionary storing student names and marks")
students = {
    "Kunal": 85,
    "Rahul": 90,
    "Amit": 78,
    "Raj": 88
}
print(students)
print("------------------------------------------------")
print(" Add a new key-value pair")
students = {
    "Kunal": 85,
    "Rahul": 90
}
students["Amit"] = 78
print(students)
print("------------------------------------------------")
print(" Delete a key-value pair")
students = {
    "Kunal": 85,
    "Rahul": 90,
    "Amit": 78
}
del students["Rahul"]
print(students)
print("------------------------------------------------")
print("Merge two dictionaries")
dict1 = {
    "Kunal": 85,
    "Rahul": 90
}
dict2 = {
    "Amit": 78,
    "Raj": 88
}
merged = dict1 | dict2
print(merged)
print("------------------------------------------------")
print(" Check if a key exists")
students = {
    "Kunal": 85,
    "Rahul": 90
}
if "Kunal" in students:
    print("Key exists")
else:
    print("Key does not exist")
print("------------------------------------------------")
print(" Count word frequency in a string")
sentence = "apple banana apple mango banana apple"

words = sentence.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print(frequency)

print("------------------------------------------------")
print("Find key with maximum value")
marks = {
    "Kunal": 85,
    "Rahul": 95,
    "Amit": 78
}
print("------------------------------------------------")
maximum = max(marks, key=marks.get)
print("Highest marks:", maximum)
print("------------------------------------------------")
print(" Reverse keys and values")
students = {
    "Kunal": 85,
    "Rahul": 90,
    "Amit": 78
}

reversed_dict = {value: key for key, value in students.items()}

print(reversed_dict)

print("------------------------------------------------")
print("Update value for a specific key")
students = {
    "Kunal": 85,
    "Rahul": 90
}

students["Kunal"] = 95
print(students)
print("------------------------------------------------")
print("Convert a list of tuples into a dictionary")
data = [
    ("Kunal", 85),
    ("Rahul", 90),
    ("Amit", 78)
]

students = dict(data)
print(students)
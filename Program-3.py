"""Write a Python program to :
1. Maintain a list of 5 employee names.
2. Print each employee name in order, numbered as:
1. Name
2. Name
3. Name"""
employees = ["Alice", "Bob", "Charlie", "David", "Eve"]
index = [1,2,3,4,5]
for i, employee in enumerate(employees):
    print(f"{index[i]} . {employee}")
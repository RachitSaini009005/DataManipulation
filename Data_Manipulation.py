# Data Preparation
Employess = [
    {"name": "Akash", "age": 22, "city": "Bhopal"},
    {"name": "Rohit", "age": 25, "city": "Indore"},
    {"name": "Madhav", "age": 28, "city": "Ayodhya"}
]


filtered_Employess = [person for person in Employess if person['age'] >= 25]   # filtering the employees whose age is 25 or greater then 25

# Sorting
sorted_Employess = sorted(filtered_Employess, key=lambda x: x['city']) # over 

# Output
print("Final list of Employess:")
for person in sorted_Employess:
    print(f"Name: {person['name']}, Age: {person['age']}, City: {person['city']}")

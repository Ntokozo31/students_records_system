"""
This program stores student records (names and marks).
The outer collection is mutable, while each individual
student record is an immutable tuple.
"""


students_records = [
    ("Thando", 78),
    ("Sipho", 45),
    ("Ayanda", 92),
    ("Zanele", 63),
    ("Musa", 38)
]


print(f"Students records: {students_records}")
print(type(students_records))
print(type(students_records[0]))
print(type(students_records[0][0]))
print(type(students_records[0][1]))
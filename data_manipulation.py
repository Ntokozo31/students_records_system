"""
This program manipulate students records,
print the reults
"""


students_records = [
    ("Thando", 78),
    ("Sipho", 45),
    ("Ayanda", 92),
    ("Zanele", 63),
    ("Musa", 38)
]


students_records.append(("Lebo", 81))
print(students_records)
students_records[1] = ("Sipho", 55)
print(students_records)
del students_records[4]
print(students_records)
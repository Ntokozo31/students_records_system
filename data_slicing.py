"""
This prohram retrieves student's records
by using slicing only
"""


students_records = [
    ("Thando", 78),
    ("Sipho", 45),
    ("Ayanda", 92),
    ("Zanele", 63),
    ("Musa", 38)
]


print(f"First three students: {students_records[0:3]}")
print(f"Last two students: {students_records[3:]}")
print(f"All students exept first student: {students_records[1:]}")
print(f"Retrieves students in reversed order: {students_records[::-1]}")
print(f"Student from Sipho through Zanele: {students_records[1:4]}")
"""
This file unpack student data, slice it
and print unpacking, slicing
"""


students_records = [
    ("Thando", 78),
    ("Sipho", 45),
    ("Ayanda", 92),
    ("Zanele", 63),
    ("Musa", 38)
]

# Slice
first_two_students_records = students_records[0:2]
last_two_students_records = students_records[3:]


# Unpack
first_student, second_student = first_two_students_records
second_last_student, last_student = last_two_students_records
print(first_student)
print(second_student)
print(second_last_student)
print(last_student)
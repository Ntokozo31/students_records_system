"""
This program retrieves data, unpacks it
and print it.
"""


students_records = [
    ("Thando", 78),
    ("Sipho", 45),
    ("Ayanda", 92),
    ("Zanele", 63),
    ("Musa", 38)
]


student_name,student_mark = students_records[0]
print(student_name)
print(student_mark)

student_name, student_mark = students_records[2]
print(student_name)
print(student_mark)

student_name, student_mark = students_records[-1]
print(student_name)
print(student_mark)
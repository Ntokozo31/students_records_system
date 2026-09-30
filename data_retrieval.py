"""
This program retrieves data from students records
using indexing only
"""


students_records = [
    ("Thando", 78),
    ("Sipho", 45),
    ("Ayanda", 92),
    ("Zanele", 63),
    ("Musa", 38)
]

print(f"First student records: {students_records[0]}")
print(f"Last student records: {students_records[-1]}")
print(f"Ayanda's marks are: {students_records[2][1]}")
print(f"Musa's name: {students_records[-1][0]}")
print(f"Second student's marks: {students_records[1][1]}")
print(f"Third student'scomplete record: {students_records[2]}")
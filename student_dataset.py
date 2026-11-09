"""
CUL-CYB 371 - Data Mining and Data Warehousing
Assignment Two: Fictional Student Dataset

This program creates a fictional dataset of students and saves it
as a CSV file named students.csv.
"""

import csv

students = [
    ["STU001", "Cybersecurity", 300, 92, 84],
    ["STU002", "Computer Science", 200, 85, 76],
    ["STU003", "Information Technology", 100, 78, 69],
    ["STU004", "Software Engineering", 300, 96, 91],
    ["STU005", "Cybersecurity", 200, 88, 79],
    ["STU006", "Computer Science", 100, 73, 65],
    ["STU007", "Data Science", 300, 90, 87],
    ["STU008", "Information Technology", 200, 81, 72],
    ["STU009", "Software Engineering", 100, 94, 89],
    ["STU010", "Data Science", 200, 86, 80],
]

headers = [
    "Student ID",
    "Department",
    "Level",
    "Attendance Percentage",
    "Average Examination Score",
]

with open("students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(students)

print("Student dataset created successfully.")
print("Total students:", len(students))

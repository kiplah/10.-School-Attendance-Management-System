# Import necessary libraries
import matplotlib.pyplot as plt
from datetime import datetime

# Function to collect attendance data
def input_attendance():
    attendance_data = {}
    while True:
        name = input("Enter student name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break
        date = input("Enter date (YYYY-MM-DD): ")
        status = input("Enter attendance status (present/absent): ").strip().lower()
        
        if name not in attendance_data:
            attendance_data[name] = []
        attendance_data[name].append((date, status))
    return attendance_data

# Function to calculate attendance percentage for each student
def calculate_attendance_percentage(attendance_data):
    percentages = {}
    for student, records in attendance_data.items():
        total_days = len(records)
        present_days = sum(1 for _, status in records if status == 'present')
        percentages[student] = (present_days / total_days) * 100 if total_days > 0 else 0
    return percentages


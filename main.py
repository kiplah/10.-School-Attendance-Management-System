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


import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import matplotlib.pyplot as plt

# Initialize attendance data dictionary
attendance_data = {}

# Function to add attendance data
def add_attendance():
    name = entry_name.get()
    date = entry_date.get()
    status = entry_status.get().lower()
    
    if name and date and status:
        if name not in attendance_data:
            attendance_data[name] = []
        attendance_data[name].append((date, status))
        
        # Clear the input fields
        entry_name.delete(0, tk.END)
        entry_date.delete(0, tk.END)
        entry_status.delete(0, tk.END)
        
        messagebox.showinfo("Success", f"Attendance for {name} on {date} added.")
    else:
        messagebox.showwarning("Input Error", "Please fill all fields.")

# Function to calculate and display attendance percentages
def show_attendance():
    percentages = {name: (sum(1 for d, s in days if s == 'present') / len(days)) * 100
                   for name, days in attendance_data.items()}
    
    # Display attendance percentages in a message box
    attendance_summary = "\n".join([f"{name}: {percent:.2f}%" for name, percent in percentages.items()])
    messagebox.showinfo("Attendance Summary", attendance_summary)
    
    # Plot attendance as a bar chart
    names = list(percentages.keys())
    values = list(percentages.values())
    
    plt.figure(figsize=(10, 5))
    plt.bar(names, values, color='skyblue')
    plt.xlabel("Student")
    plt.ylabel("Attendance Percentage")
    plt.title("Class Attendance")
    plt.show()

# Tkinter GUI setup
root = tk.Tk()
root.title("School Attendance Management System")

# Labels and Entry Fields
tk.Label(root, text="Student Name:").grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Date (YYYY-MM-DD):").grid(row=1, column=0, padx=5, pady=5)
entry_date = tk.Entry(root)
entry_date.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Attendance Status (present/absent):").grid(row=2, column=0, padx=5, pady=5)
entry_status = tk.Entry(root)
entry_status.grid(row=2, column=1, padx=5, pady=5)

# Buttons
btn_add = tk.Button(root, text="Add Attendance", command=add_attendance)
btn_add.grid(row=3, column=0, columnspan=2, pady=10)

btn_show = tk.Button(root, text="Show Attendance Summary", command=show_attendance)
btn_show.grid(row=4, column=0, columnspan=2, pady=10)

# Run the Tkinter loop
root.mainloop()

import tkinter as tk
from datetime import date

def calculate_age():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        dob = date(year, month, day)
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

        result_label.config(text=f"Your age is: {age} years")
    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numbers.")

root = tk.Tk()
root.title("Age Calculator")

tk.Label(root, text="Enter Date of Birth").grid(row=0, columnspan=2)

tk.Label(root, text="Day:").grid(row=1, column=0)
day_entry = tk.Entry(root)
day_entry.grid(row=1, column=1)

tk.Label(root, text="Month:").grid(row=2, column=0)
month_entry = tk.Entry(root)
month_entry.grid(row=2, column=1)

tk.Label(root, text="Year:").grid(row=3, column=0)
year_entry = tk.Entry(root)
year_entry.grid(row=3, column=1)

calc_button = tk.Button(root, text="Calculate Age", command=calculate_age)
calc_button.grid(row=4, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=5, columnspan=2)

root.mainloop()

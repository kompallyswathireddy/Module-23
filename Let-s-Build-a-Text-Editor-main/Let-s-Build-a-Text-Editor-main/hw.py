import tkinter as tk

def calculate_interest():
    try:
        principal = float(principal_entry.get())
        time = float(time_entry.get())
        rate = float(rate_entry.get())

        simple_interest = (principal * time * rate) / 100

        compound_interest = principal * ((1 + rate / 100) ** time) - principal

        result_label.config(text=f"Simple Interest: {simple_interest:.2f}\nCompound Interest: {compound_interest:.2f}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numbers.")

root = tk.Tk()
root.title("Interest Calculator")

tk.Label(root, text="Principal Amount:").grid(row=0, column=0)
principal_entry = tk.Entry(root)
principal_entry.grid(row=0, column=1)

tk.Label(root, text="Time Period (years):").grid(row=1, column=0)
time_entry = tk.Entry(root)
time_entry.grid(row=1, column=1)

tk.Label(root, text="Rate of Interest (% per year):").grid(row=2, column=0)
rate_entry = tk.Entry(root)
rate_entry.grid(row=2, column=1)

calc_button = tk.Button(root, text="Calculate Interest", command=calculate_interest)
calc_button.grid(row=3, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=4, columnspan=2)

root.mainloop()

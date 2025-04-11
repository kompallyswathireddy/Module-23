import tkinter as tk

def multiply_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_label.config(text=f"Product: {product}")
    except ValueError:
        result_label.config(text="Invalid input. Enter numbers only.")

root = tk.Tk()
root.title("Multiplication App")

tk.Label(root, text="Enter First Number:").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Enter Second Number:").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

calc_button = tk.Button(root, text="Multiply", command=multiply_numbers)
calc_button.grid(row=2, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=3, columnspan=2)

root.mainloop()

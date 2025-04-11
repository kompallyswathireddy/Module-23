import tkinter as tk

def convert_to_cm():
    try:
        inches = float(entry.get())
        cm = inches * 2.54  
        result_label.config(text=f"Length in cm: {cm:.2f}")
    except ValueError:
        result_label.config(text="Invalid input. Enter a number.")

root = tk.Tk()
root.title("Inches to Centimeters Converter")

tk.Label(root, text="Enter length in inches:").grid(row=0, column=0)
entry = tk.Entry(root)
entry.grid(row=0, column=1)

convert_button = tk.Button(root, text="Convert", command=convert_to_cm)
convert_button.grid(row=1, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=2, columnspan=2)

root.mainloop()

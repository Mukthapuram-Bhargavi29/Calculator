import tkinter as tk
from tkinter import messagebox


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == "add":
            result = add(num1, num2)
        elif operation == "subtract":
            result = subtract(num1, num2)
        elif operation == "multiply":
            result = multiply(num1, num2)
        elif operation == "divide":
            result = divide(num1, num2)

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")
    except ZeroDivisionError as e:
        messagebox.showerror("Math Error", str(e))



root = tk.Tk()
root.title("Structured Tkinter Calculator")
root.geometry("350x300")

tk.Label(root, text="Enter First Number:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter Second Number:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack()

tk.Button(root, text="Add", width=15, command=lambda: calculate("add")).pack(pady=5)
tk.Button(root, text="Subtract", width=15, command=lambda: calculate("subtract")).pack(pady=5)
tk.Button(root, text="Multiply", width=15, command=lambda: calculate("multiply")).pack(pady=5)
tk.Button(root, text="Divide", width=15, command=lambda: calculate("divide")).pack(pady=5)

result_label = tk.Label(root, text="Result: ", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

root.mainloop()
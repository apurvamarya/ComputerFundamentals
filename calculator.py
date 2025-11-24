import tkinter as tk
from tkinter import messagebox

# Function to handle button clicks
def on_button_click(char):
    current_text = entry.get()

    if char == "C":
        # Clear the entry
        entry.delete(0, tk.END)
    elif char == "=":
        try:
            # Evaluate the expression
            result = str(eval(current_text))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
    else:
        # Append the character to the entry
        entry.insert(tk.END, char)

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display expression / result
entry = tk.Entry(root, width=25, font=("Arial", 18), borderwidth=5, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button labels in a grid layout
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "C", "+"
]

# Create buttons dynamically
row = 1
col = 0
for char in buttons:
    button = tk.Button(
        root,
        text=char,
        width=5,
        height=2,
        font=("Arial", 16),
        command=lambda ch=char: on_button_click(ch)
    )
    button.grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

# = button (big at bottom)
equal_button = tk.Button(
    root,
    text="=",
    width=22,
    height=2,
    font=("Arial", 16),
    command=lambda: on_button_click("=")
)
equal_button.grid(row=row, column=0, columnspan=4, padx=5, pady=10)

# Start the GUI event loop
root.mainloop()

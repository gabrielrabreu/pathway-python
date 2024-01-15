import tkinter as tk

# Function to calculate the result
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)  # Clear the input box
        entry.insert(tk.END, str(result))  # Display the result
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to add characters to the input box
def add_to_input(char):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + char)

# Create a Tkinter window
root = tk.Tk()
root.title("Calculator")

# Create an input box
entry = tk.Entry(root, width=20)
entry.grid(row=0, column=0, columnspan=4)

# Create numeric and operator buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Add buttons to the interface
row, col = 1, 0
for button in buttons:
    if button == '=':
        tk.Button(root, text=button, command=calculate).grid(row=row, column=col)
    else:
        tk.Button(root, text=button, command=lambda b=button: add_to_input(b)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Start the main Tkinter loop
root.mainloop()

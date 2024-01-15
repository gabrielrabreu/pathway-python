import tkinter as tk

# Create a Tkinter window
root = tk.Tk()
root.title("Tkinter Example")

# Create a label widget
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

# Create a button widget
button = tk.Button(root, text="Click Me!", command=lambda: label.config(text="Button Clicked!"))
button.pack()

# Start the Tkinter main loop
root.mainloop()

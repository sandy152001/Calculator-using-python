import tkinter as tk

# Function to update the expression in the entry box
def update_expression(num):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + str(num))

# Function to clear the entry box
def clear_entry():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def calculate():
    try:
        expression = entry.get()
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create an entry widget to display the expression
entry = tk.Entry(window, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Create the buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0

for button in buttons:
    if button == '=':
        btn = tk.Button(window, text=button, width=10, height=3, command=calculate)
    else:
        btn = tk.Button(window, text=button, width=10, height=3, 
                        command=lambda b=button: update_expression(b))
    
    btn.grid(row=row, column=col, sticky="nsew")
    
    col += 1
    if col > 3:
        col = 0
        row += 1

# Create a clear button
clear_button = tk.Button(window, text="C", width=10, height=3, command=clear_entry)
clear_button.grid(row=row, column=0, columnspan=4, sticky="nsew")

# Run the application
window.mainloop()

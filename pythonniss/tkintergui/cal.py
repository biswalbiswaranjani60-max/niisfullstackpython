import tkinter as tk

# Create window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Entry field
entry = tk.Entry(root, width=25, font=("Arial", 20), borderwidth=5, relief="ridge")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to click buttons
def click(num):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(num))

# Clear function
def clear():
    entry.delete(0, tk.END)

# Calculate result
def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Buttons
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
]

# Create buttons
for (text, row, col) in buttons:
    if text == "=":
        tk.Button(root, text=text, padx=20, pady=20, command=equal).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, padx=20, pady=20,
                  command=lambda t=text: click(t)).grid(row=row, column=col)

# Clear button
tk.Button(root, text="C", padx=20, pady=20, command=clear).grid(row=5, column=0, columnspan=4, sticky="we")

# Run app
root.mainloop()
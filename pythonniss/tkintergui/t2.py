import tkinter as tk

root = tk.Tk()
root.title("Addition App")
root.geometry("300x200")

# First number
entry1 = tk.Entry(root)
entry1.pack()

# Second number
entry2 = tk.Entry(root)
entry2.pack()

# Function to add
def add():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result = num1 + num2
    label.config(text="Result: " + str(result))

# Button
button = tk.Button(root, text="Add", command=add)
button.pack()

# Result label
label = tk.Label(root, text="")
label.pack()

root.mainloop()
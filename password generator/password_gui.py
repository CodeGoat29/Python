import random
import string
import tkinter as tk

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))

def generate():
    try:
        length = int(length_entry.get())
        result = generate_password(length)
        password_label.config(text=result)
    except ValueError:
        password_label.config(text="Enter a number")

root = tk.Tk()
root.title("Password Generator")

instruction_label = tk.Label(root, text="Enter password length:")
instruction_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate)
generate_button.pack()

password_label = tk.Label(root, text="", font=("Arial", 14))
password_label.pack()

root.mainloop()

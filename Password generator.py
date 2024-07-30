import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())
    options = []

    if use_uppercase.get():
        options.append(string.ascii_uppercase)
    if use_lowercase.get():
        options.append(string.ascii_lowercase)
    if use_digits.get():
        options.append(string.digits)
    if use_special.get():
        options.append(string.punctuation)

    if not options:
        messagebox.showwarning("Input Error", "Select at least one character type.")
        return

    all_characters = "".join(options)
    password = "".join(random.choice(all_characters) for _ in range(length))
    result_label.config(text=f"Generated Password: {password}")

root = tk.Tk()
root.title("Password Generator")


length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=5)

length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=5)

use_uppercase = tk.BooleanVar()
uppercase_check = tk.Checkbutton(root, text="Include Uppercase", variable=use_uppercase)
uppercase_check.grid(row=1, column=0, padx=10, pady=5, sticky='w')

use_lowercase = tk.BooleanVar()
lowercase_check = tk.Checkbutton(root, text="Include Lowercase", variable=use_lowercase)
lowercase_check.grid(row=1, column=1, padx=10, pady=5, sticky='w')

use_digits = tk.BooleanVar()
digits_check = tk.Checkbutton(root, text="Include Digits", variable=use_digits)
digits_check.grid(row=2, column=0, padx=10, pady=5, sticky='w')

use_special = tk.BooleanVar()
special_check = tk.Checkbutton(root, text="Include Special Characters", variable=use_special)
special_check.grid(row=2, column=1, padx=10, pady=5, sticky='w')

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Generated Password: ")
result_label.grid(row=4, column=0, columnspan=2, pady=10)
root.mainloop()

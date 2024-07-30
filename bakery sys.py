import tkinter as tk
from tkinter import messagebox

menu = {
    'Pizza': 100,
    'Burger': 80,
    'Sandwich': 60,
    'Shawarma': 70,
    'Drink': 30
}

order_details = {}
order_total = 0

def update_order_summary():
    order_summary.delete(1.0, tk.END)
    total = 0
    for item, quantity in order_details.items():
        cost = menu[item] * quantity
        order_summary.insert(tk.END, f"{item} (x{quantity}): Rs {cost}\n")
        total += cost
    order_summary.insert(tk.END, f"Total amount: Rs {total}")

def add_item():
    global order_total
    item = item_var.get()
    if item not in menu:
        messagebox.showerror("Error", "Item not available!")
        return

    try:
        quantity = int(quantity_var.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid quantity.")
        return

    if item in order_details:
        order_details[item] += quantity
    else:
        order_details[item] = quantity
    order_total += menu[item] * quantity
    update_order_summary()
    messagebox.showinfo("Item Added", f'{quantity} {item}(s) added to your order.')

def remove_item():
    global order_total
    item = item_var.get()
    if item not in order_details:
        messagebox.showwarning("Item Not Found", f'{item} is not in your current order.')
        return

    try:
        quantity = int(quantity_var.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid quantity.")
        return

    if quantity >= order_details[item]:
        order_total -= menu[item] * order_details[item]
        del order_details[item]
        messagebox.showinfo("Item Removed", f'All {item}(s) removed from your order.')
    else:
        order_details[item] -= quantity
        order_total -= menu[item] * quantity
        messagebox.showinfo("Item Removed", f'{quantity} {item}(s) removed from your order.')
    update_order_summary()

def finish_order():
    update_order_summary()
    messagebox.showinfo("Order Finished", f'Final receipt:\n{order_summary.get(1.0, tk.END)}')
    root.destroy()

root = tk.Tk()
root.title("Bakery Order System")

tk.Label(root, text="Welcome to our Bakery!").grid(row=0, columnspan=2)
tk.Label(root, text="Menu").grid(row=1, columnspan=2)

row = 2
for item, price in menu.items():
    tk.Label(root, text=f"{item}: Rs {price}").grid(row=row, columnspan=2)
    row += 1

tk.Label(root, text="Enter item:").grid(row=row, column=0)
item_var = tk.StringVar(root)
item_entry = tk.Entry(root, textvariable=item_var)
item_entry.grid(row=row, column=1)

row += 1
tk.Label(root, text="Enter quantity:").grid(row=row, column=0)
quantity_var = tk.StringVar(root)
quantity_entry = tk.Entry(root, textvariable=quantity_var)
quantity_entry.grid(row=row, column=1)

row += 1
tk.Button(root, text="Add Item", command=add_item).grid(row=row, column=0)
tk.Button(root, text="Remove Item", command=remove_item).grid(row=row, column=1)

row += 1
order_summary = tk.Text(root, height=10, width=40)
order_summary.grid(row=row, columnspan=2)

row += 1
tk.Button(root, text="Finish Order", command=finish_order).grid(row=row, columnspan=2)

root.mainloop()

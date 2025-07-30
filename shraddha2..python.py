import tkinter as tk
from tkinter import ttk, messagebox

# Hardcoded exchange rates
rates = {
    "USD": 1.0,
    "INR": 83.0,
    "EUR": 0.92,
    "GBP": 0.79,
    "JPY": 157.5
}

def convert_currency():
    try:
        from_curr = from_currency.get().upper()
        to_curr = to_currency.get().upper()
        amt = float(amount.get())

        if from_curr not in rates or to_curr not in rates:
            messagebox.showerror("Error", "Invalid currency code!")
            return

        from_rate = rates[from_curr]
        to_rate = rates[to_curr]
        usd_amount = amt / from_rate
        converted = usd_amount * to_rate

        # Clear previous table rows
        for row in tree.get_children():
            tree.delete(row)

        # Insert new row
        tree.insert("", "end", values=(from_curr, to_curr, amt, f"{converted:.2f}"))

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# GUI Setup
root = tk.Tk()
root.title("Currency Converter")
root.geometry("500x400")

# Input fields
tk.Label(root, text="From Currency (USD, INR, EUR, GBP, JPY):").pack()
from_currency = tk.Entry(root)
from_currency.pack()

tk.Label(root, text="To Currency:").pack()
to_currency = tk.Entry(root)
to_currency.pack()

tk.Label(root, text="Amount:").pack()
amount = tk.Entry(root)
amount.pack()

tk.Button(root, text="Convert", command=convert_currency).pack(pady=10)

# Table Output
columns = ("From", "To", "Amount", "Converted")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100, anchor='center')
tree.pack(pady=20)

root.mainloop()

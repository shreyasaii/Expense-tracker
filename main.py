import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

# Function to handle 'Add Expense' button click
def add_expense():
    try:
        amount = float(amount_entry.get())
        category = category_var.get()
        description = description_entry.get()
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Add expense to listbox with description
        expense_entry = f"{date} - {category}: ${amount:.2f} - {description}"
        expenses_listbox.insert(tk.END, expense_entry)
        
        # Update total expenses
        expense_amounts.append(amount)
        total_expenses.set(f"Total Expenses: ${sum(expense_amounts):.2f}")
        
        # Clear input fields
        amount_entry.delete(0, tk.END)
        description_entry.delete(0, tk.END)
        
        messagebox.showinfo("Expense Added", "Expense successfully added!")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount.")

# Function to handle 'Delete Expense' button click
def delete_expense():
    try:
        selected_index = expenses_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Select Expense", "Please select an expense to delete.")
            return
        
        # Get selected expense and remove from listbox
        selected_expense = expenses_listbox.get(selected_index)
        expenses_listbox.delete(selected_index)
        
        # Extract amount from selected expense and update total expenses
        amount_str = selected_expense.split("$")[-1].split()[0]
        amount = float(amount_str)
        expense_amounts.remove(amount)
        total_expenses.set(f"Total Expenses: ${sum(expense_amounts):.2f}")
        
        messagebox.showinfo("Expense Deleted", "Expense successfully deleted.")
    except Exception as e:
        messagebox.showerror("Error", f"Error deleting expense: {str(e)}")

# Function to handle 'Generate Report' button click
def generate_report():
    # Calculate total expenses and display
    total = sum(expense_amounts)
    total_expenses.set(f"Total Expenses: ${total:.2f}")
    
    # Display message box with total expenses
    messagebox.showinfo("Total Expenses", f"Your total expenses are: ${total:.2f}")

# Initialize GUI
root = tk.Tk()
root.title("Expense Tracker")

# Variables
expense_amounts = []

# GUI Components
style = ttk.Style()
style.configure('TButton', font=('Arial', 12), padding=5)
style.configure('TLabel', font=('Arial', 12))

frame_entry = tk.Frame(root)
frame_entry.pack(padx=20, pady=10)

amount_label = ttk.Label(frame_entry, text="Amount:")
amount_label.grid(row=0, column=0, padx=5, pady=5, sticky="W")

amount_entry = ttk.Entry(frame_entry, font=('Arial', 12), width=15)
amount_entry.grid(row=0, column=1, padx=5, pady=5)

description_label = ttk.Label(frame_entry, text="Description:")
description_label.grid(row=1, column=0, padx=5, pady=5, sticky="W")

description_entry = ttk.Entry(frame_entry, font=('Arial', 12), width=30)
description_entry.grid(row=1, column=1, padx=5, pady=5)

category_label = ttk.Label(frame_entry, text="Category:")
category_label.grid(row=2, column=0, padx=5, pady=5, sticky="W")

categories = ["Groceries", "Utilities", "Transportation", "Entertainment", "Other"]
category_var = tk.StringVar(root)
category_var.set(categories[0])

category_dropdown = ttk.Combobox(frame_entry, textvariable=category_var, values=categories, font=('Arial', 12), width=27)
category_dropdown.grid(row=2, column=1, padx=5, pady=5)

add_expense_button = ttk.Button(frame_entry, text="Add Expense", command=add_expense, style='TButton')
add_expense_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10, sticky="WE")

delete_expense_button = ttk.Button(frame_entry, text="Delete Expense", command=delete_expense, style='TButton')
delete_expense_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10, sticky="WE")

frame_listbox = tk.Frame(root)
frame_listbox.pack(padx=20, pady=10)

expenses_listbox = tk.Listbox(frame_listbox, width=70, height=10, font=('Arial', 12))
expenses_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame_listbox, orient=tk.VERTICAL)
scrollbar.config(command=expenses_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

expenses_listbox.config(yscrollcommand=scrollbar.set)

frame_report = tk.Frame(root)
frame_report.pack(padx=20, pady=10)

generate_report_button = ttk.Button(frame_report, text="Generate Report", command=generate_report, style='TButton')
generate_report_button.pack()

total_expenses = tk.StringVar()
total_expenses.set("Total Expenses: $0.00")
total_expenses_label = ttk.Label(frame_report, textvariable=total_expenses, font=('Arial', 14, 'bold'))
total_expenses_label.pack()

# Start GUI main loop
root.mainloop()

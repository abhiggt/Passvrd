import tkinter as tk
from subprocess import call
from tkinter import simpledialog, messagebox, ttk

# The keyword to unlock the vault
SECRET_KEYWORD = "1234"

# Function to check the keyword and open the vault
def check_keyword():
    user_input = simpledialog.askstring("Keyword", "Enter the keyword:")
    if user_input == SECRET_KEYWORD:
        open_vault()
        
    else:
        messagebox.showerror("Error", "Incorrect keyword!")

# Function to open the vault GUI
def open_vault():
    vault_window = tk.Toplevel(root)
    vault_window.title("Vault")
    vault_window.configure(bg='#111111')
    
    # Data storage
    vault_data = {}

    def pswrd():
	    call(['python','passvrd.py'])
	    pswrd()

    # Function to add entry to the vault
    def add_entry():
        account = account_entry.get()
        password = password_entry.get()
        if account and password:
            if account in vault_data:
                messagebox.showwarning("Warning", "Account already exists!")
            else:
                vault_data[account] = password
                table.insert("", "end", values=(account, password))
                account_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)
                
        else:
            messagebox.showwarning("Warning", "Please enter both account and password!")

    # Function to delete selected entry from the vault
    def delete_entry():
        selected_item = table.selection()
        if selected_item:
            account = table.item(selected_item)["values"][0]
            del vault_data[account]
            table.delete(selected_item)
        else:
            messagebox.showwarning("Warning", "Please select an entry to delete!")

    # UI Elements
    account_label = tk.Label(vault_window, text="Account:", fg="#5ced9b", bg='#111111', font=("Product Sans", 15))
    account_label.grid(row=0, column=0, padx=10, pady=10)
    
    account_entry = tk.Entry(vault_window,text="enter Account:", fg="black", bg = "grey" , font=("Product Sans", 15))
    account_entry.grid(row=0, column=1, padx=10, pady=10)

    password_label = tk.Label(vault_window, text="Password:", fg="#5ced9b", bg='#111111', font=("Product Sans", 15))
    password_label.grid(row=1, column=0, padx=10, pady=10)
    
    password_entry = tk.Entry(vault_window,text="enter pass:", fg="black", bg = "grey" , font=("Product Sans", 15))
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    add_button = tk.Button(vault_window, text="Add Entry", command=add_entry, fg="#5ced9b", bg='#111111', font=("Product Sans", 13))
    add_button.grid(row=2, column=0, columnspan=1, pady=10)

    delete_button = tk.Button(vault_window, text="Delete Entry", command=delete_entry, fg="#5ced9b", bg='#111111', font=("Product Sans", 13))
    delete_button.grid(row=2, column=1, columnspan=1, pady=10)

    open_password_button = tk.Button(vault_window, text="Open Passvrd", command=pswrd,fg="#5ced9b", bg='#111111', font=("Product Sans", 13), compound=tk.LEFT)
    open_password_button.grid(row=6, column=0, columnspan=2, pady=10)

    # Table to display account and password
    columns = ("Account", "Password")
    table = ttk.Treeview(vault_window, columns=columns, show='headings')
    table.heading("Account", text="Account")
    table.heading("Password", text="Password")
    table.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    # Style configuration for the table
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", 
                    background="grey",
                    foreground="white",
                    rowheight=25,
                    fieldbackground="#111111")
    style.map("Treeview", background=[("selected", "teal")])

# Root window setup
root = tk.Tk()
root.withdraw()  # Hide the root window

# Start the keyword check dialog
check_keyword()

# Start the main event loop
root.mainloop()

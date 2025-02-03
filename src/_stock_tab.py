import tkinter as tk
from tkinter import ttk

class _stock_tab(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master=master
        #self.master = master
        #self.master.title("Stock Management System")
        #self.master.geometry("600x400")

        self.stock_data = []  # List to store stock items

        self.create_widgets()

    def create_widgets(self):
        """Create UI Elements"""
        #frame = tk.Frame(self.master)
        #frame.pack(pady=10)

        tk.Label(self, text="Name").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self, text="Quantity").grid(row=0, column=1, padx=5, pady=5)
        tk.Label(self, text="Price").grid(row=0, column=2, padx=5, pady=5)

        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=1, column=0, padx=5, pady=5)

        self.quantity_entry = tk.Entry(self)
        self.quantity_entry.grid(row=1, column=1, padx=5, pady=5)

        self.price_entry = tk.Entry(self)
        self.price_entry.grid(row=1, column=2, padx=5, pady=5)

        tk.Button(self, text="Add", command=self.add_item, bg="green", fg="white").grid(row=1, column=3, padx=5, pady=5)
        tk.Button(self, text="Update", command=self.update_item, bg="blue", fg="white").grid(row=1, column=4, padx=5, pady=5)
        tk.Button(self, text="Delete", command=self.delete_item, bg="red", fg="white").grid(row=1, column=5, padx=5, pady=5)

        # Table (Treeview)
        columns = ("Name", "Quantity", "Price")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("Price", text="Price")
        self.tree.grid(row=2, column=0, columnspan=5, sticky="ew", padx=10, pady=5)

    def add_item(self):
        """Add a new stock item"""
        name = self.name_entry.get()
        quantity = self.quantity_entry.get()
        price = self.price_entry.get()

        if name and quantity.isdigit() and price.replace(".", "", 1).isdigit():
            self.stock_data.append([name, int(quantity), float(price)])
            self.update_table()
            self.clear_entries()
        else:
            messagebox.showerror("Input Error", "Please enter valid data.")

    def update_item(self):
        """Update selected stock item"""
        selected = self.tree.focus()
        if selected:
            values = self.tree.item(selected, "values")
            for item in self.stock_data:
                if item[0] == values[0]:  # Find the item by name
                    item[1] = int(self.quantity_entry.get())
                    item[2] = float(self.price_entry.get())
                    self.update_table()
                    self.clear_entries()
                    return
            messagebox.showwarning("Not Found", "Item not found in stock.")
        else:
            messagebox.showwarning("Selection Error", "Select an item to update.")

    def delete_item(self):
        """Delete selected stock item"""
        selected = self.tree.focus()
        if selected:
            values = self.tree.item(selected, "values")
            self.stock_data[:] = [item for item in self.stock_data if item[0] != values[0]]  # Remove item
            self.update_table()
            self.clear_entries()
        else:
            messagebox.showwarning("Selection Error", "Select an item to delete.")

    def update_table(self):
        """Refresh the stock table"""
        self.tree.delete(*self.tree.get_children())  # Clear table
        for item in self.stock_data:
            self.tree.insert("", "end", values=item)

    def clear_entries(self):
        """Clear input fields"""
        self.name_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        


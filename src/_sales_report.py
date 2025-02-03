import tkinter as tk
from tkinter import ttk, messagebox
import csv

class SalesReportFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill="both", expand=True)

        # Sample Sales Data (Date, Product, Quantity, Price)
        self.sales_data = [
            ("2024-01-01", "Product A", 10, 25.5),
            ("2024-01-05", "Product B", 5, 40.0),
            ("2024-01-10", "Product C", 8, 30.75),
            ("2024-01-15", "Product A", 12, 25.5),
            ("2024-01-20", "Product D", 7, 50.0),
        ]

        self.create_widgets()
        self.populate_table()

    def create_widgets(self):
        """Creates the UI components inside the frame"""
        # Search Bar
        frame_top = tk.Frame(self)
        frame_top.pack(pady=10)

        tk.Label(frame_top, text="Search:").pack(side=tk.LEFT, padx=5)
        self.entry_search = tk.Entry(frame_top, width=30)
        self.entry_search.pack(side=tk.LEFT, padx=5)

        btn_search = tk.Button(frame_top, text="Search", command=self.search_sales)
        btn_search.pack(side=tk.LEFT, padx=5)

        btn_refresh = tk.Button(frame_top, text="Refresh", command=self.populate_table)
        btn_refresh.pack(side=tk.LEFT, padx=5)

        # Sales Data Table
        columns = ("Date", "Product", "Quantity", "Price")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=130)

        self.tree.pack(pady=10, fill="both", expand=True)

        # Summary Section
        self.lbl_total_sales = tk.Label(self, text="Total Sales: $0.00", font=("Arial", 12, "bold"))
        self.lbl_total_sales.pack(pady=5)

        # Export Button
        btn_export = tk.Button(self, text="Export to CSV", command=self.export_to_csv)
        btn_export.pack(pady=10)

    def populate_table(self):
        """Fills the table with sales data"""
        for row in self.tree.get_children():
            self.tree.delete(row)
        for sale in self.sales_data:
            self.tree.insert("", "end", values=sale)
        self.update_summary()

    def search_sales(self):
        """Filters sales data based on search query"""
        query = self.entry_search.get().lower()
        for row in self.tree.get_children():
            self.tree.delete(row)
        for sale in self.sales_data:
            if query in str(sale[0]).lower() or query in str(sale[1]).lower():
                self.tree.insert("", "end", values=sale)
        self.update_summary()

    def update_summary(self):
        """Calculates and updates total sales"""
        total = sum(row[2] * row[3] for row in self.sales_data)
        self.lbl_total_sales.config(text=f"Total Sales: ${total:.2f}")

    def export_to_csv(self):
        """Exports sales data to a CSV file"""
        filename = "monthly_sales_report.csv"
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Product", "Quantity", "Price"])
            for row in self.sales_data:
                writer.writerow(row)
        messagebox.showinfo("Export", f"Sales report saved as {filename}")



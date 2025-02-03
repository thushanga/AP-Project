import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from _home_window import _home_window
from _login_window import _login_window


class _root_window(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title('Penguin Pharmacy-Your wellbeing is our first priority')
        self.geometry("1400x800");
        self.page1=_login_window(self)
        self.page2=_home_window(self)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.page1.grid(row=1, column=1)
        
        
        
            
                # Create a Menu bar
        self.menu_bar = tk.Menu(self)

        # Register Menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Supplier", command=self.add_supplier)
        self.file_menu.add_command(label="Medicine", command=self.add_medicine)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_app)
        self.menu_bar.add_cascade(label="Register", menu=self.file_menu)

        # Edit Menu
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Total Sales", command=self.undo_action)
        self.edit_menu.add_command(label="Stock")
        self.menu_bar.add_cascade(label="Report", menu=self.edit_menu)

        # Help Menu
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="About", command=self.about_app)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)

        # Attach the menu bar to the window
        self.config(menu=self.menu_bar)
   
        
    def submit_form(self):
        name = entry_name.get()
        address = entry_address.get()

        if name and address:
            messagebox.showinfo("Success", f"Supplier Added:\n\nName: {name}\nAddress: {address}")
            entry_name.delete(0, tk.END)
            entry_address.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please fill in all fields.")
        
    def center_window(self,window, width=300, height=200):
        # Get screen width and height
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        
        # Calculate position x, y
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        
        # Set geometry
        window.geometry(f"{width}x{height}+{x}+{y}")
    
        # Function for menu actions
    def add_supplier(self):
        new_window = tk.Toplevel(self)
        new_window.title("Register Supplier")
        new_window.geometry("400x200")

                # Supplier Name
        tk.Label(new_window, text="Supplier Name:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        entry_name = tk.Entry(new_window, width=30)
        entry_name.grid(row=0, column=1, padx=10, pady=5)

        # Supplier Address
        tk.Label(new_window, text="Supplier Address:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        entry_address = tk.Entry(new_window, width=30)
        entry_address.grid(row=1, column=1, padx=10, pady=5)

        # Submit Button
        btn_submit = tk.Button(new_window, text="Add Supplier")
        btn_submit.grid(row=2, column=0, columnspan=2, pady=10)


    def add_medicine(self):
        new_window = tk.Toplevel(self)
        new_window.title("Register Medicine")
        new_window.geometry("400x200")

        # Supplier Name
        tk.Label(new_window, text="Medicine Name:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        entry_name = tk.Entry(new_window, width=30)
        entry_name.grid(row=0, column=1, padx=10, pady=5)
        
        # Supplier Name
        tk.Label(new_window, text="Medicine Code:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        entry_code = tk.Entry(new_window, width=30)
        entry_code.grid(row=1, column=1, padx=10, pady=5)
        
        # Supplier Name
        tk.Label(new_window, text="Select Supplier:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        # Dropdown (Combobox)
        options = ["Option 1", "Option 2", "Option 3", "Option 4"]
        combo = ttk.Combobox(new_window, values=options, state="readonly")
        combo.grid(row=2, column=1, padx=10, pady=5)
        combo.current(0)  # Set default value
        

        # Supplier Address
        #tk.Label(new_window, text="Supplier Address:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        #entry_address = tk.Entry(new_window, width=30)
        #entry_address.grid(row=3, column=1, padx=10, pady=5)

        # Submit Button
        btn_submit = tk.Button(new_window, text="Register")
        btn_submit.grid(row=4, column=1, columnspan=2, pady=10)

    def exit_app():
        root.quit()

    
    def undo_action(self):
       pass

    def about_app():
        messagebox.showinfo("About", "This is a Tkinter menu example.")

    def draw_widgets(self):
        login_frame = tk.Frame(self._root_window, relief="groove", bd=3, padx=10, pady=10)
        login_frame.grid(row=0, column=0, padx=20, pady=20)
                                   
        # Function to validate the login
    def navigate_login(self):
        self.page1.grid_forget()
        #self.page2.grid(row=1,column=1)
        self.page2.grid(row=0, column=0, columnspan=3,rowspan=3,sticky='nesw')
        self.grid_columnconfigure(0,weight=1)
        
# Create an instance of the MyGUI class.
if __name__ == "__main__":
    pharmacy = _root_window()
    pharmacy.mainloop()
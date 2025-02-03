import tkinter as tk
from tkinter import messagebox

class _login_window(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master=master
        self['borderwidth'] = 1
        self['relief'] = 'ridge'
        self.title_label = tk.Label(self, text="Welcome & Login", font=("Arial", 20, "bold"), fg="blue")
        self.title_label.grid(row=0, column=0, padx=10, pady=5,sticky="e",columnspan=2)  # Center it with padding
        self.username_label = tk.Label(self, text="Userid:")
        self.username_label.grid(row=1, column=0, padx=10, pady=5,sticky="e")
        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=1, column=1, padx=10, pady=5, sticky="e")
        self.password_label = tk.Label(self, text="Password:")
        self.password_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=2, column=1, padx=10, pady=5, sticky="e")
        self.login_button = tk.Button(self, text="Login", command=self.do_login)
        self.login_button.grid(row=3, column=1, padx=0, pady=5, sticky="e")
        self.exit_button = tk.Button(self, text="Quit",command=master.destroy)
        self.exit_button.grid(row=3, column=1, padx=65, pady=5, sticky="e")
        
    def do_login(self):
        userid = self.username_entry.get()
        password = self.password_entry.get()

        if userid == "admin" and password == "admin":
            self.master.navigate_login()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
from datetime import datetime


class _home_window(tk.Frame):
    
    def __init__(self,master):
        super().__init__(master)
        self.config(bg="skyblue")
        
        paned = tk.PanedWindow(self, orient="vertical")
        paned.pack(fill="both", expand=True)
        
        #top_frame = tk.Frame(paned, bg="lightblue", height=150)
        top_frame = tk.PanedWindow(paned, orient="horizontal",height=500,width=1400)
        top_frame.pack(fill="both", expand=True)
        
        
        left_frame = tk.Frame(top_frame, bg="lightblue",height=500,width=700)
        #left_frame.pack(side="left", fill="both")
        #tk.Label(left_frame, text="Enter Your Name:").pack(pady=5)
        #self.name_entry = tk.Entry(left_frame)
        #self.name_entry.pack()
        #self.datetime_label = tk.Label(left_frame, text="", font=("Arial", 12), fg="blue")
        #self.datetime_label.pack()
        #self.update_datetime()
        self.edit_save=tk.Label(left_frame,text="Prescription Information",width=87)
        self.edit_save.pack()
        self.update_datetime()
        # Name Label & Entry
        tk.Label(left_frame, text="Name:(Required)").pack(anchor="w", pady=2)
        name_entry = tk.Entry(left_frame)
        name_entry.pack(fill="x", pady=2)

        # Email Label & Entry
        tk.Label(left_frame, text="Email:(Optional)").pack(anchor="w", pady=2)
        email_entry = tk.Entry(left_frame)
        email_entry.pack(fill="x", pady=2)

        # Telephone Label & Entry
        tk.Label(left_frame, text="Telephone:(Optional)").pack(anchor="w", pady=2)
        telephone_entry = tk.Entry(left_frame)  
        telephone_entry.pack(fill="x", pady=2)
        
        # Sample Data for Dropdown
        self.items = ["Apple", "Banana", "Blueberry", "Cherry", "Grapes", "Mango", "Orange", "Peach", "Pear", "Watermelon"]

        # Label
        tk.Label(left_frame, text="Select a Medicine:").pack(anchor="w", pady=2)

        # Searchable Combobox
        self.combo_var = tk.StringVar()
        self.combo_box = ttk.Combobox(left_frame, textvariable=self.combo_var, values=self.items)
        self.combo_box.pack(fill="x", pady=2)

        # Bind Key Release Event for Dynamic Filtering
        self.combo_box.bind("<KeyRelease>", self.filter_dropdown)
        
        
        # Telephone Label & Entry
        tk.Label(left_frame, text="Dosage:").pack(anchor="w", pady=2)
        dosage_entry = tk.Entry(left_frame)  
        dosage_entry.pack(fill="x", pady=2)

        
        # DateTime Label & Entry
        #tk.Label(left_frame, text="Date/Time:(Required)").pack(anchor="w", pady=2)
        #self.datetime_label = tk.Entry(left_frame)
        #self.datetime_entry.pack(fill="x", pady=2)
        #self.update_datetime()
        
        #self.datetime_label = tk.Label(left_frame)
        #self.datetime_label.pack(fill="x", pady=2)
        

        # Submit Button
        clear_button = tk.Button(left_frame, text="Clear")
        clear_button.pack(side=tk.RIGHT, padx=5)
        # Submit Button
        submit_button = tk.Button(left_frame, text="Save")
        submit_button.pack(side=tk.RIGHT, padx=5)



        
        
        right_frame = tk.Frame(top_frame, bg="lightgreen",height=500,width=700)
        #right_frame.pack(side="right", fill="both", expand=True)
        self.upload_button = tk.Button(right_frame, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(pady=10)
        self.close_button = tk.Button(right_frame, text="Close", command=master.destroy)
        self.close_button.pack(pady=10)
        self.image_label = tk.Label(right_frame)
        self.image_label.pack(pady=10)
        
        top_frame.add(left_frame)
        top_frame.add(right_frame)
        paned.add(top_frame)
        
        bottom_frame = tk.Frame(paned, bg="lightgreen",height=300)
        self.table = ttk.Treeview(bottom_frame, columns=("Name", "Age", "City"), show="headings")
        self.table.pack(fill="both", expand=True)
        self.table.heading("Name", text="Name")
        self.table.heading("Age", text="Age")
        self.table.heading("City", text="City")
        data = [("Alice", 25, "New York"), 
        ("Bob", 30, "San Francisco"), 
        ("Charlie", 22, "Los Angeles")]
        for row in data:
            self.table.insert("", "end", values=row)
            
        paned.add(bottom_frame)
 
 
    def filter_dropdown(self, event):
        """Filters dropdown items based on user input."""
        typed_text = self.combo_var.get().lower()
        filtered_items = [item for item in self.items if typed_text in item.lower()]
        
        # Update the dropdown values
        self.combo_box['values'] = filtered_items
        
    def filter_dropdown(self, event):
        """Filters dropdown items based on user input."""
        typed_text = self.combo_var.get().lower()
        filtered_items = [item for item in self.items if typed_text in item.lower()]
        
        # Update the dropdown values
        self.combo_box['values'] = filtered_items
    def update_datetime(self):
        """Update the current date and time every second."""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.edit_save.config(text=f"Prescription Information : {now}")
        self.after(1000, self.update_datetime)  # Schedule update every second

    def upload_image(self):
        
        
        # Open file dialog to select an image
        file_path = filedialog.askopenfilename(filetypes=[("Image Files",  "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
        print(file_path)
    
        if file_path:
            # Open and resize the image
            img = Image.open(file_path)
            img = img.resize((600, 400))  # Resize image to fit in label
            
            # Convert the image to Tkinter format
            img_tk = ImageTk.PhotoImage(img)
            
            # Update the label with the new image
            self.image_label.config(image=img_tk)
            self.image_label.image = img_tk  # Keep a reference

import tkinter as tk
from tkinter import messagebox

def authenticate():
    username = username_entry.get()
    password = password_entry.get()

    if username == "client" and password == "server":
        messagebox.showinfo("Login Successful", "Welcome, client!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create main window
root = tk.Tk()
root.title("Login Screen")
root.geometry("300x200")

# Username Label and Entry
username_label = tk.Label(root, text="Username:")
username_label.pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

# Password Label and Entry
password_label = tk.Label(root, text="Password:")
password_label.pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

# Login Button
login_button = tk.Button(root, text="Login", command=authenticate)
login_button.pack(pady=10)

# Run the application
root.mainloop()
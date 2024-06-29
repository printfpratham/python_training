#! /usr/bin/python3

import hashlib
import os
import tkinter as tk
from tkinter import messagebox

# Function to hash a password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to save username and hashed password to a file
def save_user_credentials(username, password, filename='user_credentials.txt'):
    hashed_password = hash_password(password)
    with open(filename, 'a+') as file:
        file.write(f"{username}:{hashed_password}\n")

# Function to verify user credentials
def verify_user_credentials(username, password, filename='user_credentials.txt'):
    hashed_password = hash_password(password)
    if not os.path.exists(filename):
        return False
    
    with open(filename, 'r') as file:
        for line in file:
            saved_username, saved_hashed_password = line.strip().split(':')
            if saved_username == username and saved_hashed_password == hashed_password:
                return True
    return False

# Function to read file contents
def read_file_contents(filename='my_file.txt'):
    if not os.path.exists(filename):
        return "File not found."
    
    with open(filename, 'r') as file:
        return file.read()

# Function to handle saving credentials
def save_credentials():
    username = entry_username.get()
    password = entry_password.get()
    if username and password:
        save_user_credentials(username, password)
        messagebox.showinfo("Success", "Credentials saved successfully.")
    else:
        messagebox.showwarning("Input Error", "Please enter both username and password.")

# Function to handle verifying credentials and displaying file contents
def verify_credentials():
    username = entry_username_verify.get()
    password = entry_password_verify.get()
    if username and password:
        if verify_user_credentials(username, password):
            messagebox.showinfo("Access Granted", "Access granted.")
            display_file_contents()
        else:
            messagebox.showwarning("Access Denied", "Access denied. Invalid username or password.")
    else:
        messagebox.showwarning("Input Error", "Please enter both username and password.")

# Function to display file contents in the GUI
def display_file_contents():
    contents = read_file_contents()
    text_display.config(state=tk.NORMAL)
    text_display.delete('1.0', tk.END)
    text_display.insert(tk.END, contents)
    text_display.config(state=tk.DISABLED)

# Main GUI
root = tk.Tk()
root.title("Password Manager")

# Frame for saving credentials
frame_save = tk.Frame(root, padx=10, pady=10)
frame_save.pack(padx=10, pady=10)

label_username = tk.Label(frame_save, text="Enter username:")
label_username.grid(row=0, column=0, pady=5)
entry_username = tk.Entry(frame_save)
entry_username.grid(row=0, column=1, pady=5)

label_password = tk.Label(frame_save, text="Enter password:")
label_password.grid(row=1, column=0, pady=5)
entry_password = tk.Entry(frame_save, show="*")
entry_password.grid(row=1, column=1, pady=5)

button_save = tk.Button(frame_save, text="Save Credentials", command=save_credentials)
button_save.grid(row=2, columnspan=2, pady=10)

# Frame for verifying credentials
frame_verify = tk.Frame(root, padx=10, pady=10)
frame_verify.pack(padx=10, pady=10)

label_username_verify = tk.Label(frame_verify, text="Enter username to verify:")
label_username_verify.grid(row=0, column=0, pady=5)
entry_username_verify = tk.Entry(frame_verify)
entry_username_verify.grid(row=0, column=1, pady=5)

label_password_verify = tk.Label(frame_verify, text="Enter password to verify:")
label_password_verify.grid(row=1, column=0, pady=5)
entry_password_verify = tk.Entry(frame_verify, show="*")
entry_password_verify.grid(row=1, column=1, pady=5)

button_verify = tk.Button(frame_verify, text="Verify Credentials", command=verify_credentials)
button_verify.grid(row=2, columnspan=2, pady=10)

# Frame for displaying file contents
frame_display = tk.Frame(root, padx=10, pady=10)
frame_display.pack(padx=10, pady=10)

text_display = tk.Text(frame_display, height=10, width=50, state=tk.DISABLED)
text_display.pack()

root.mainloop()


import tkinter as tk
from tkinter import messagebox
import os

DATA_FILE = "covid_tracing_data.txt"

def submit_data():
    name = name_entry.get()
    location = location_entry.get()
    date = date_entry.get()
    contact = contact_entry.get()

    if name and location and date and contact:
        with open(DATA_FILE, "a") as file:
            file.write(f"{name},{location},{date},{contact}\n")
        messagebox.showinfo("Data Submitted", "Contact tracing information saved successfully!")
        clear_entries()
    else:
        messagebox.showerror("Error", "Please fill out all fields.")

def clear_entries():
    name_entry.delete(0, tk.END)
    location_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)

def search_data():
    search_name = search_entry.get()
    if not search_name:
        messagebox.showerror("Error", "Please enter a name to search.")
        return
    
    with open(DATA_FILE, "r") as file:
        lines = file.readlines()
        found_entries = [line.strip().split(",") for line in lines if search_name.lower() in line.lower()]

    if found_entries:
        messagebox.showinfo("Search Results", format_search_results(found_entries))
    else:
        messagebox.showinfo("Search Results", "No matching entries found.")

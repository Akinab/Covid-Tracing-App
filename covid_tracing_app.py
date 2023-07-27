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

def format_search_results(entries):
    results = "Search Results:\n"
    for entry in entries:
        results += f"Name: {entry[0]}, Location: {entry[1]}, Date: {entry[2]}, Contact: {entry[3]}\n"
    return results

def create_gui():
    global name_entry, location_entry, date_entry, contact_entry, search_entry

    root = tk.Tk()
    root.title("COVID Contact Tracing App")
    root.geometry("500x300")

    # Set a background image
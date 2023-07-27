import tkinter as tk
from tkinter import messagebox
import os

DATA_FILE = "covid_tracing_data.txt"

def submit_data():
    name = name_entry.get()
    location = location_entry.get()
    date = date_entry.get()
    contact = contact_entry.get()
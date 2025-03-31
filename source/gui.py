import tkinter as tk
from tkinter import filedialog, messagebox
import os
from files import copy_model_file, load_file_names
from prepare import process_file

def select_input():
    input_file = filedialog.askopenfilename(
        title="Select CSV File", 
        filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
    )
    if input_file:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, input_file)

def select_output():
    output_file = filedialog.asksaveasfilename(
        title="Select Output File", 
        defaultextension=".csv",
        filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
    )
    if output_file:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, output_file)

def run_processing():
    input_file = input_entry.get()
    # output_file = output_entry.get()
    if not input_file:
        messagebox.showerror("Error", "Please select an input file.")
        return
    print (input_file)

    # Convert to an absolute path
    absolute_path = os.path.abspath(input_file)
    print("Absolute Path:", absolute_path)

    # Get the directory name of the path
    directory = os.path.dirname(absolute_path)
    print("Directory:", directory)

    # Get the base name (file or last folder) of the path
    base_name = os.path.basename(absolute_path)
    print("Base Name:", base_name)
    try:
        process_file(input_file, directory)
        messagebox.showinfo("Success", f"File processed successfully!\nOutput saved to:\n{directory}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")

# Build the GUI.
root = tk.Tk()
root.title("CSV Processor")

# Create a label, entry, and button for the input file.
tk.Label(root, text="Select the Interlocks file:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
input_entry = tk.Entry(root, width=50)
input_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Browse...", command=select_input).grid(row=0, column=2, padx=5, pady=5)

# Create a label, entry, and button for the output file.
tk.Label(root, text="Output CSV File:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
output_entry = tk.Entry(root, width=50)
output_entry.grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="Browse...", command=select_output).grid(row=1, column=2, padx=5, pady=5)

# Create the process button.
tk.Button(root, text="Process File", command=run_processing).grid(row=2, column=1, padx=5, pady=10)

root.mainloop()

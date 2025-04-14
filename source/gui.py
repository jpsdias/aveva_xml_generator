import tkinter as tk
from tkinter import filedialog, messagebox
import os
from source.generate import copy_model_file
from source.prepare import process_file

def select_input():
    input_file = filedialog.askopenfilename(
        title="Select CSV File", 
        filetypes=[("CSV Files", "*.csv")]
    )
    if input_file:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, input_file)

def select_model():
    input_model = filedialog.askopenfilename(
        title="Select XML File", 
        filetypes=[("XML Files", "*.xml")]
    )
    if input_model:
        input_entry_model.delete(0, tk.END)
        input_entry_model.insert(0, input_model)

def select_output():
    # Open a folder selection dialog and update the entry with the chosen folder path
    folder_path = filedialog.askdirectory(title="Select Output Folder")
    if folder_path:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, folder_path)

def run_processing():
    input_file = input_entry.get()
    if not input_file:
        messagebox.showerror("Error", "Please select an input file.")
        return

    # Convert to an absolute path
    input_abs_path = os.path.abspath(input_file)

    try:
        namesList = process_file(input_abs_path)
        messagebox.showinfo("Success", f"File processed successfully!\n")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")

    model_file = input_entry_model.get()
    if not model_file:
        messagebox.showerror("Error", "Please select a model file.")
        return
    
     # Convert to an absolute path
    model_abs_path = os.path.abspath(model_file)

    output_file = output_entry.get()
    if not output_file:
        messagebox.showerror("Error", "Please select an output file.")
        return
    
    # Convert to an absolute path
    output_abs_path = os.path.abspath(output_file)

    print(namesList)
    # Copy the model file for each valve.
    copy_model_file(model_abs_path, namesList, output_abs_path)

# Build the GUI.
root = tk.Tk()
root.title("XML Files Generator")

# Create a label, entry, and button for the input file.
tk.Label(root, text="Interlocks file:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
input_entry = tk.Entry(root, width=50)
input_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Browse...", command=select_input).grid(row=0, column=2, padx=5, pady=5)

# Create a label, entry, and button for the input file.
tk.Label(root, text="Model file:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
input_entry_model = tk.Entry(root, width=50)
input_entry_model.grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="Browse...", command=select_model).grid(row=1, column=2, padx=5, pady=5)

# Create a label, entry, and button for the output file.
tk.Label(root, text="Output Folder:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
output_entry = tk.Entry(root, width=50)
output_entry.grid(row=2, column=1, padx=5, pady=5)
tk.Button(root, text="Browse...", command=select_output).grid(row=2, column=2, padx=5, pady=5)

# Create the process button.
tk.Button(root, text="Generate", command=run_processing).grid(row=3, column=1, padx=5, pady=10)

root.mainloop()

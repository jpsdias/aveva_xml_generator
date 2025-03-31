import tkinter as tk
from tkinter import filedialog, messagebox
import os

def process_file(input_file, output_file):
    # Open the input file with the appropriate encoding.
    with open(input_file, 'r', encoding='latin-1') as f:
        lines = f.readlines()

    processed_lines = []
    # Process each line with its line number (starting at 1).
    for i, line in enumerate(lines, start=1):
        # Skip the first 5 lines.
        if i <= 5:
            continue

        # Strip whitespace.
        line_stripped = line.strip()
        # Skip empty lines.
        if not line_stripped:
            continue

        # Exclude lines that contain "_SecuIntlk".
        if "_SecuIntlk" in line_stripped:
            continue

        # Keep only the text before the first comma (if present).
        if ',' in line_stripped:
            new_line = line_stripped.split(',', 1)[0]
        else:
            new_line = line_stripped

        # Only add nonempty lines.
        if new_line:
            processed_lines.append(new_line + "\n")

    # Write the processed lines to the output file.
    with open(output_file, 'w', encoding='latin-1') as f:
        f.writelines(processed_lines)

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
    output_file = output_entry.get()
    if not input_file or not output_file:
        messagebox.showerror("Error", "Please select both an input and an output file.")
        return

    try:
        process_file(input_file, output_file)
        messagebox.showinfo("Success", f"File processed successfully!\nOutput saved to:\n{output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")

# Build the GUI.
root = tk.Tk()
root.title("CSV Processor")

# Create a label, entry, and button for the input file.
tk.Label(root, text="Input CSV File:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
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

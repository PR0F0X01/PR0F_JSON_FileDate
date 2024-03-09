#!/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog
import json

class JsonEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("JSON Editor")

        # File path for reading and writing
        self.file_path = None

        # Widgets
        self.choose_file_button = tk.Button(master, text="Choose JSON File", command=self.choose_json_file)
        self.choose_file_button.pack(pady=10)

        self.load_arrays_button = tk.Button(master, text="Load Arrays", command=self.load_arrays)
        self.load_arrays_button.pack(pady=10)

        self.add_array_button = tk.Button(master, text="Add Array", command=self.add_array)
        self.add_array_button.pack(pady=10)

        self.save_button = tk.Button(master, text="Save Data", command=self.save_data)
        self.save_button.pack(pady=10)

        # Entry widgets for data
        self.selected_array_var = tk.StringVar()
        self.array_dropdown = tk.OptionMenu(master, self.selected_array_var, "")
        self.array_dropdown.pack(pady=10)

        self.new_array_label = tk.Label(master, text="New Array Name:")
        self.new_array_label.pack()
        self.new_array_entry = tk.Text(master, height=8, width=90)
        self.new_array_entry.pack()

        self.name_label = tk.Label(master, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Text(master, height=12, width=90)
        self.name_entry.pack()

        self.value_label = tk.Label(master, text="Value:")
        self.value_label.pack()
        self.value_entry = tk.Text(master, height=12, width=90)
        self.value_entry.pack()

    def choose_json_file(self):
        # Step 1: Choose JSON File
        self.file_path = filedialog.askopenfilename(title="Select JSON File", filetypes=[("JSON files", "*.json")])

    def load_arrays(self):
        # Step 2: Load Arrays and populate the dropdown menu
        if self.file_path:
            try:
                with open(self.file_path, 'r') as file:
                    data = json.load(file)
                    array_names = list(data.keys())

                if array_names:
                    self.array_dropdown['menu'].delete(0, 'end')  # Clear the current menu
                    for array_name in array_names:
                        self.array_dropdown['menu'].add_command(label=array_name, command=tk._setit(self.selected_array_var, array_name))
                else:
                    print("No arrays found in the selected file.")
            except json.JSONDecodeError:
                print("Invalid JSON format in the selected file.")
        else:
            print("Please choose a JSON file.")

    def add_array(self):
        # Step 3: Add a new empty array for each line in the "New Array" entry
        if self.file_path:
            new_array_names = self.new_array_entry.get("1.0", "end-1c").strip().split('\n')

            if new_array_names:
                try:
                    with open(self.file_path, 'r') as file:
                        existing_data = json.load(file)
                
                    for new_array_name in new_array_names:
                        existing_data[new_array_name] = {}

                    with open(self.file_path, 'w') as file:
                        json.dump(existing_data, file, indent=2, separators=(',', ': '))
                    self.load_arrays()  # Update the array dropdown
                except (FileNotFoundError, json.JSONDecodeError):
                    print("Error adding new arrays.")
            else:
                print("Please enter at least one name for the new array.")
        else:
            print("Please choose a JSON file.")

    def save_data(self):
        # Step 4: Save Data to the selected array based on the entered data
        selected_array = self.selected_array_var.get()
        if self.file_path and selected_array:
            name_lines = self.name_entry.get("1.0", "end-1c").strip().split('\n')
            value_lines = self.value_entry.get("1.0", "end-1c").strip().split('\n')

            if len(name_lines) == len(value_lines):
                data = dict(zip(name_lines, value_lines))

                try:
                    with open(self.file_path, 'r') as file:
                        existing_data = json.load(file)
                        for name, value in data.items():
                            existing_data[selected_array][name] = value
                except (FileNotFoundError, json.JSONDecodeError, KeyError):
                    print(f"Error updating data in array '{selected_array}'.")
                    return

                with open(self.file_path, 'w') as file:
                    json.dump(existing_data, file, indent=2, separators=(',', ': '))
            else:
                print("Number of names and values should match.")
        else:
            print("Please choose a JSON file and select an array.")

# Create the main window
root = tk.Tk()
app = JsonEditor(root)
root.mainloop()
# @by prof0x01

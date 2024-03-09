#Welcome to PR0F_JSON_FileDate 

`PR0F_JSON_FileDate.py`, is a JSON editor built using the Tkinter library. It provides a graphical user interface (GUI) for easily manipulating and adding data to JSON files. Here's an overview of its features:

### Key Features:

1. **File Selection:**
   - Allows users to choose a JSON file through a file dialog.

2. **Load Arrays:**
   - Reads the selected JSON file and populates a dropdown menu with the available array names.

3. **Add Array:**
   - Adds new empty arrays to the JSON file based on the user-provided array names.

4. **Save Data:**
   - Saves data to the selected array within the JSON file, utilizing the entered name-value pairs.

### GUI Components:

- **Choose JSON File Button:**
  - Initiates the file dialog for selecting a JSON file.

- **Load Arrays Button:**
  - Loads available arrays from the selected JSON file.

- **Add Array Button:**
  - Adds new arrays to the JSON file based on user input.

- **Save Data Button:**
  - Saves data to the selected array in the JSON file.

- **Dropdown Menu:**
  - Displays available array names for selection.

- **Entry Widgets:**
  - Collects input for new array names, and name-value pairs for data to be saved.

### Usage:

1. **Choose JSON File:**
   - Click the "Choose JSON File" button to select a JSON file.

2. **Load Arrays:**
   - After selecting a file, use the "Load Arrays" button to populate the dropdown menu with array names.

3. **Add Array:**
   - Enter new array names in the "New Array Name" text field and click the "Add Array" button.

4. **Save Data:**
   - Select an array from the dropdown, enter name-value pairs, and click the "Save Data" button.
  
   - 
# Installing and Running the Program

## Step 1: Download the Program

```
git clone https://github.com/PR0F0X01/PR0F_JSON_FileDate
cd PR0F_JSON_FileDate
```

## Step 2: Install Requirements

```
pip3 install -r requirements.txt
```

This command will install all the libraries listed in the `requirements.txt` file.

## Step 3: run PR0F_JSON_FileDate.py


```
python3 PR0F_JSON_FileDate.py
```

### Notes:

- The program ensures proper matching of names and values during data entry.
- Exception handling is implemented to manage potential errors like invalid JSON format or missing files.

Feel free to utilize this JSON editor to streamline your JSON file manipulation tasks. For any assistance,  [@pr0f0x01] (https://twitter.com/pr0f0x01). 

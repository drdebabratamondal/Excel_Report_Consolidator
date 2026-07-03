import pandas as pd
import numpy as np
import os
import glob
import json
from openpyxl.utils import column_index_from_string

try:
    with open('config.json', 'r') as file:
        config = json.load(file)
except FileNotFoundError:
    print("Error: config.json not found. Please create it in the project folder.")
    exit()

folder_path = config.get('folder_path', './data')

# 1. Identify all available Excel files
search_pattern = os.path.join(folder_path, "*.xlsx")
excel_files = glob.glob(search_pattern)

if not excel_files:
    print("No Excel files found in the data folder.")
    exit()

# 2. Let the user choose the master file
print("--- Available Files ---")
for i, file in enumerate(excel_files):
    print(f"{i + 1}: {os.path.basename(file)}")

try:
    choice = int(input("\nSelect the number of the file to use as the master template: ")) - 1
    master_path = excel_files[choice]
    master_file = os.path.basename(master_path)
    print(f"Master file set to: {master_file}")
except (ValueError, IndexError):
    print("Invalid selection.")
    exit()

# 3. Prompt user for Excel grid boundaries
print("\n--- Grid Configuration ---")
try:
    excel_row_start = int(input("Enter starting row number (e.g., 6): "))
    excel_row_end = int(input("Enter ending row number (e.g., 194): "))
    col_start_letter = input("Enter starting column letter (e.g., E): ")
    col_end_letter = input("Enter ending column letter (e.g., S): ")
    
    row_start = excel_row_start - 1
    row_end = excel_row_end
    col_start = column_index_from_string(col_start_letter) - 1
    col_end = column_index_from_string(col_end_letter)
except ValueError:
    print("Invalid input. Please ensure rows are numbers and columns are letters.")
    exit()

# 4. Perform consolidation
df_summed = pd.read_excel(master_path, sheet_name='Sheet1', header=None)

for file in excel_files:
    file_name = os.path.basename(file)
    
    # Skip the chosen master and the output file
    if file_name in [master_file, "Consolidated_Master_Report.xlsx"]:
        continue
        
    print(f"Processing: {file_name}")
    try:
        df_temp = pd.read_excel(file, sheet_name='Sheet1', header=None)
        
        for r in range(row_start, row_end):
            for c in range(col_start, col_end):
                val_current = pd.to_numeric(df_summed.iloc[r, c], errors='coerce')
                val_new = pd.to_numeric(df_temp.iloc[r, c], errors='coerce')
                
                if np.isnan(val_current): val_current = 0
                if np.isnan(val_new): val_new = 0
                
                df_summed.iloc[r, c] = val_current + val_new
    except Exception as e:
        print(f"Skipping {file_name} due to error: {e}")

output_path = os.path.join(folder_path, "Consolidated_Master_Report.xlsx")
df_summed.to_excel(output_path, index=False, header=False)
print(f"\nConsolidation complete. File saved to {output_path}")
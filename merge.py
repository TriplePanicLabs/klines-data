import csv
import os
import pandas as pd
from pathlib import Path
from collections import defaultdict

def merge_csv_files(root_dir):
    files_dict = defaultdict(list)
    
    # Step 1: Recursively find all CSV files
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.csv'):
                base_name = '-'.join(file.split('-')[:-1])  # Remove the part after the last '-'
                files_dict[base_name].append(os.path.join(root, file))
    
    # Step 2: Merge files with the same base name
    for base_name, file_paths in files_dict.items():
        combined_df = pd.concat([pd.read_csv(fp) for fp in sorted(file_paths)], ignore_index=True)
        
        # Step 3: Save the merged file
        output_path = os.path.join(root_dir, f"{base_name}.csv")
        combined_df.to_csv(output_path, index=False)
        print(f"Merged files into {output_path}")


dirs = ["data", "btc"]
for dir in dirs:
    merge_csv_files(dir)
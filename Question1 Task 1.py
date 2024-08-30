import zipfile
import os

# Define the zip file location and extraction path
zip_file_path = r"C:\Users\arifu\Desktop\Assignment 2.zip"
extracted_dir = r"C:\Users\arifu\Desktop\Assignment_2"

# Unzip the folder
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extracted_dir)

print("Extraction completed!")


import pandas as pd
import os

# Path to the directory containing CSV files
csv_directory = extracted_dir
output_file = 'extracted_text.txt'

with open(output_file, 'w') as outfile:
    for filename in os.listdir(csv_directory):
        if filename.endswith('.csv'):
            # Read the CSV file
            df = pd.read_csv(os.path.join(csv_directory, filename))
            # Check if 'SHORT-TEXT' column exists
            if 'SHORT-TEXT' in df.columns:
                # Extract the text from 'SHORT-TEXT' column
                text_column = df['SHORT-TEXT']
                text_data = '\n'.join(text_column.dropna().astype(str).tolist())
                outfile.write(text_data + '\n')

                print("Everything good!")
    print(f"Text extracted and saved to: {os.path.abspath(output_file)}")
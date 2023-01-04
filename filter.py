#imports
import os
import csv

#variables
absolute_path = os.path.dirname(__file__)

#functions

#fuction which returns a full file path based on a relative path
def full_path(relative_path):
  return os.path.join(absolute_path, relative_path)

def filter_pink_morsels(data_folder):
  # Iterate over the files in the data folder
  for file in os.listdir(data_folder):
    # Check if the file is a CSV file
    if file.endswith('.csv'):
      # Open the file for reading
      with open(os.path.join(data_folder, file), 'r', encoding='utf-8') as f:
        # Create a list to store the rows that we want to keep
        filtered_rows = []
        # Create a CSV reader
        reader = csv.reader(f)
        # Iterate over the rows in the file
        for row in reader:
          # Check if the item name contains 'pink morsel'
          if 'pink morsel' in row[0]:
            # If it does, add it to the list
            filtered_rows.append(row)

      # Open the file for writing
      with open(os.path.join(data_folder, file), 'w', encoding='utf-8') as f:
        # Create a CSV writer
        writer = csv.writer(f)
        # Write the filtered rows back to the file
        writer.writerows(filtered_rows)


filter_pink_morsels(full_path('data'))

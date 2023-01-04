#imports
import os
import csv

#variables
absolute_path = os.path.dirname(__file__)

#functions

#function which returns a full file path based on a relative path
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

def multiply_columns(data_folder, col1, col2):
  # Iterate over the files in the data folder
  for file in os.listdir(data_folder):
    # Check if the file is a CSV file
    if file.endswith('.csv'):
      # Open the file for reading
      with open(os.path.join(data_folder, file), 'r', encoding='utf-8') as f:
        # Create a list to store the modified rows
        modified_rows = []
        # Create a CSV reader
        reader = csv.reader(f)
        # Iterate over the rows in the file
        for row in reader:
          # Remove all non-digit characters from the value in the second column
          value1 = row[col1].replace('$', '').replace(',', '')
          # Multiply the values in the specified columns
          result = int(value1) * int(row[col2])
          # Add the "$" symbol back to the result
          result = "${}".format(result)
          # Replace the values in the row with the result
          row[col1] = result
          row[col2] = result
          # Add the modified row to the list
          modified_rows.append(row)

      # Open the file for writing
      with open(os.path.join(data_folder, file), 'w', encoding='utf-8') as f:
        # Create a CSV writer
        writer = csv.writer(f)
        # Write the modified rows back to the file
        writer.writerows(modified_rows)

def modify_columns(data_folder, col1):
  # Iterate over the files in the data folder
  for file in os.listdir(data_folder):
    # Check if the file is a CSV file
    if file.endswith('.csv'):
      # Open the file for reading
      with open(os.path.join(data_folder, file), 'r', encoding='utf-8') as f:
        # Create a list to store the modified rows
        modified_rows = []
        # Create a CSV reader
        reader = csv.reader(f)
        # Iterate over the rows in the file
        for row in reader:
          # Remove all non-digit characters from the value in the second column
          value1 = row[col1].replace('$', '').replace(',', '').replace('.', '')
          # Divide the value in the second column by 100
          # value1 = int(value1) / 1000
          # Add the "$" symbol back to the result
          value1 = "${}".format(value1)
          # Replace the value in the second column with the result
          row[col1] = value1
          # Remove the third column
          del row[2]
          # Add the modified row to the list
          modified_rows.append(row)
    # Open the file for writing
    with open(os.path.join(data_folder, file), 'w', encoding='utf-8') as f:
      # Create a CSV writer
      writer = csv.writer(f)
      # Write the modified rows back to the file
      writer.writerows(modified_rows)


filter_pink_morsels(full_path('data'))
# multiply_columns(full_path('data'), 1, 2)
# modify_columns(full_path('data'), 1)


<h1>Completing an Internship with Copilot and ChatGPT</h1>

With the GitHub Sudent Developer pack, I have access to Copilot, which I am running as a VSCode Extension. I shall attempt to complete this internship program with as little actual code writing as possible, using as much AI assistance as possible, and intervening where necessary.

<h2>First Task</h2>
In order to filter the csv files to only include transactions of pink morsels, I entered the following comment in to the top of the file #create a function which filters all three csv files in the ./data folder to only include transactions with pink morsels
It creates one line of code: def filter_pink_morsels(): and then gives up, as it cannot seem to process the rest of the function. At this point, I handed the task off the ChatGPT to see how it would handle it.

ChatGPT returned a much more complete function:

```python
import csv

def filter_pink_morsels(data_folder):
#Create a list to store the filtered rows
filtered_rows = []

# Iterate over the files in the data folder
for file in os.listdir(data_folder):
    # Check if the file is a CSV file
    if file.endswith(".csv"):
    # Open the file
    with open(os.path.join(data_folder, file), "r") as f:
        # Create a CSV reader
        reader = csv.reader(f)
        # Iterate over the rows in the file
        for row in reader:
        # Check if the item name contains "pink morsels"
        if "pink morsels" in row[2]:
            # If it does, add it to the list
            filtered_rows.append(row)
        # Return the list of filtered rows
        return filtered_rows
```
It told me I could run it using the command `filtered_rows = filter_pink_morsels("./data")`
Immediately, it threw up the error `NameError: name 'os' is not defined`, which I fixed by adding `import os` to the top of the file. (This suggestion was automatically filled in by copilot while documenting the error)
<br>
I asked ChatGPT to modify the code so that it deleted all entries not containing pink morsels, and it returned the following:

```python
def filter_pink_morsels(data_folder):
  # Iterate over the files in the data folder
  for file in os.listdir(data_folder):
    # Check if the file is a CSV file
    if file.endswith(".csv"):
      # Open the file
      with open(os.path.join(data_folder, file), "r") as f:
        # Create a list to store the rows that we want to keep
        filtered_rows = []
        # Create a CSV reader
        reader = csv.reader(f)
        # Iterate over the rows in the file
        for row in reader:
          # Check if the item name contains "pink morsels"
          if "pink morsels" in row[2]:
            # If it does, add it to the list
            filtered_rows.append(row)

      # Open the file for writing
      with open(os.path.join(data_folder, file), "w") as f:
        # Create a CSV writer
        writer = csv.writer(f)
        # Write the filtered rows back to the file
        writer.writerows(filtered_rows)
```
After running this file, it promplty deleted every single entry in every file. I restored it and asked ChatGPT to fix the error, and it returned the following:
```python
import csv

def filter_pink_morsels(data_folder):
  # Iterate over the files in the data folder
  for file in os.listdir(data_folder):
    # Check if the file is a CSV file
    if file.endswith(".csv"):
      # Open the file for reading
      with open(os.path.join(data_folder, file), "r") as f:
        # Create a list to store the rows that we want to keep
        filtered_rows = []
        # Create a CSV reader
        reader = csv.reader(f)
        # Iterate over the rows in the file
        for row in reader:
          # Check if the item name contains "pink morsels"
          if "pink morsels" in row[2]:
            # If it does, add it to the list
            filtered_rows.append(row)

      # Open the file for writing
      with open(os.path.join(data_folder, file), "w") as f:
        # Create a CSV writer
        writer = csv.writer(f)
        # Write the filtered rows back to the file
        writer.writerows(filtered_rows)
```
This still did not work, so I told ChatGPT that the product name in the in the first column of the csv file. It told me to change `row[2]` to `row[0]`, which I did. It also altered the `open` commands to include the "encoding" parameter, which was related to an earlier enquiry. Alas, this did stil not work. As resetting the files was getting exhausting, I asked ChatGPT to print the file to the output rather than writing it back to the file.

```python
import csv

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
        # Check if the item name contains "pink morsels"
        if 'pink morsels' in row[0]:
            # If it does, add it to the list
            filtered_rows.append(row)

    # Print the filtered rows
    for row in filtered_rows:
        print(row)
```
It was only at this point in which I realised the reason it was deleting everything was because it was looking for "pink morsels" rather than "pink morsel". I corrected this and it worked perfectly. I then reverted to the old version of the code which modified the csv files, with this alteration. This was a success, and the csv files were now filtered to only include transactions with pink morsels.
<h3>Multiplication</h3>
I then asked ChatGPT to multiply the number of pink morsels by the price of each pink morsel. Unfortunately, this was very difficult for ChatGPT to grasp, so I told it to re-write all the functions using pandas. Eventually, I got it to output this function for mulitplying two columns using pandas:

```python
import pandas as pd
import os

def multiply_columns(csv_file, col1, col2, result_col):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file, encoding='utf-8')
    
    # Remove the currency symbol from the first column
    df[col1] = df[col1].str.replace('$', '')
    
    # Convert the first column to a numeric type
    df[col1] = pd.to_numeric(df[col1])
    
    # Remove the currency symbol from the second column
    df[col2] = df[col2].str.replace('$', '')
    
    # Convert the second column to a numeric type
    df[col2] = pd.to_numeric(df[col2])
    
    # Multiply the two columns and store the result in a new column
    df[result_col] = df[col1] * df[col2]
    
    # Add the currency symbol back to the new column
    df[result_col] = '$' + df[result_col].astype(str)
    
    # Write the modified DataFrame back to the CSV file
    df.to_csv(csv_file, encoding='utf-8', index=False)
```
Unfortunately, this does not iterate over every file, so I asked it to do exactly that.
  
```python
import pandas as pd
import os

def multiply_columns(data_folder, col1, col2, result_col):
    # Iterate over the files in the data folder
    for file in os.listdir(data_folder):
        # Check if the file is a CSV file
        if file.endswith('.csv'):
            # Read the CSV file into a pandas DataFrame
            df = pd.read_csv(os.path.join(data_folder, file), encoding='utf-8')

            # Remove the currency symbol from the first column
            df[col1] = df[col1].str.replace('$', '')

            # Convert the first column to a numeric type
            df[col1] = pd.to_numeric(df[col1])

            # Remove the currency symbol from the second column
            df[col2] = df[col2].str.replace('$', '')

            # Convert the second column to a numeric type
            df[col2] = pd.to_numeric(df[col2])

            # Multiply the two columns and store the result in a new column
            df[result_col] = df[col1] * df[col2]

            # Add the currency symbol back to the new column
            df[result_col] = '$' + df[result_col].astype(str)

            # Write the modified DataFrame back to the CSV file
            df.to_csv(os.path.join(data_folder, file), encoding='utf-8', index=False)
```
Each time the code was generated, ChatGPT also returned a short description of what the code does, and how to use the function. For example, for this code, it returned the following:

>This function will loop through all the CSV files in the specified data_folder directory and multiply the specified col1 and col2 columns for each file. The result will be stored in a new column with the name specified in the result_col parameter, and the currency symbol will be added back to the new column. To use this function, pass the path to the directory containing the CSV files, the names of the two columns you want to multiply, and the name of the result column as arguments.

Whenever an error occurred, I could copy and paste the error into ChatGPT and it would attempt to re-write the code to fix it's own error. It would also point out if it was a user error or something to do with the CSV's and not the code it wrote itself.

With further adjustment using the same process and applying it for all steps as required for the task, I was able to get a working program. I manually got the function to return the dataframe, after it was done processing, then made each function take a dataframe as a parameter. This allowed me to keep the original files untouched while processing and creating the combined sales_data.
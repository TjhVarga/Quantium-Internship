import os
import pandas as pd

#variables
absolute_path = os.path.dirname(__file__)

def full_path(relative_path):
    return os.path.join(absolute_path, relative_path)

def filter_csv(data_folder, col_name, filtered_term):
    # Iterate over the files in the data folder
    for file in os.listdir(data_folder):
        # Check if the file is a CSV file
        if file.endswith('.csv'):
            # Read the CSV file into a pandas DataFrame
            df = pd.read_csv(os.path.join(data_folder, file), encoding='utf-8')

            # Filter the rows to only include transactions with the specified term
            df = df[df[col_name].str.contains(filtered_term)]

            # Drop the product name, as it is no longer needed
            df.drop(col_name, axis=1, inplace=True)

            # Write the modified DataFrame back to the CSV file
            # df.to_csv(os.path.join(data_folder, file), encoding='utf-8', index=False)
            # Return the final DataFrame
            return df

def multiply_columns(data_folder, col1, col2, result_col, dataframe):
    # Iterate over the files in the data folder
    for file in os.listdir(data_folder):
        # Check if the file is a CSV file
        if file.endswith('.csv'):
            # Read the CSV file into a pandas DataFrame
            # df = pd.read_csv(os.path.join(data_folder, file), encoding='utf-8')
            df = dataframe
            # Remove the currency symbol from the first column
            df[col1] = df[col1].str.replace('$', '')

            # Convert the first column to a numeric type
            df[col1] = pd.to_numeric(df[col1])

            # Remove the currency symbol from the first column
            # df[col2] = df[col1].str.replace('$', '')

            # Convert the second column to a numeric type
            # df[col2] = pd.to_numeric(df[col1])

            # Multiply the two columns and store the result in a new column
            df[result_col] = df[col1] * df[col2]

            # Add the currency symbol back to the new column
            df[result_col] = '$' + df[result_col].astype(str)

            # Drop the original col1 and col2 columns
            df.drop([col1, col2], axis=1, inplace=True)

            # Write the modified DataFrame back to the CSV file
            # df.to_csv(os.path.join(data_folder, file), encoding='utf-8', index=False)

            #return the final dataframe
            return df

def combine_csv(data_folder, combined_filename, dataframe):
    # Create an empty list to store the DataFrames
    df_list = []

    # Iterate over the files in the data folder
    for file in os.listdir(data_folder):
        # Check if the file is a CSV file
        if file.endswith('.csv'):
            # Read the CSV file into a pandas DataFrame
            # df = pd.read_csv(os.path.join(data_folder, file), encoding='utf-8')
            df = dataframe
            # Append the DataFrame to the list
            df_list.append(df)

    # Concatenate the DataFrames in the list into a single DataFrame
    combined_df = pd.concat(df_list, ignore_index=True)

    # Write the combined DataFrame to a CSV file
    combined_df.to_csv(os.path.join(data_folder, combined_filename), encoding='utf-8', index=False)


combine_csv(
    full_path('data'), 
    'sales_data.csv', 
    multiply_columns(full_path('data'), 'price', 'quantity', 'sales', filter_csv(full_path('data'), 'product', 'pink morsel')))

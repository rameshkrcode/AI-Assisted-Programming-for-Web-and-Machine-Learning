
import pandas as pd

def csv_to_json(csv_file, json_file, selected_columns=None):
    """ Convert CSV to JSON with missing value handling and column selection """
    df = pd.read_csv(csv_file)
    # Handle missing values by filling with an empty string
    df.fillna('', inplace=True)
    # Filter specific columns if provided
    if selected_columns:
        df = df[selected_columns]
    # Convert to JSON
    df.to_json(json_file, orient='records', indent=4)
    print(f"Successfully converted {csv_file} to {json_file}")

# Example usage
csv_to_json('data.csv', 'data.json', selected_columns=['name', 'email'])

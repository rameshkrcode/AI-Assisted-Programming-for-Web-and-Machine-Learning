
import pandas as pd

def generate_sales_report(csv_file, output_file):
    """ Aggregates sales data by region and exports a summary """
    df = pd.read_csv(csv_file)
    # Group sales by region and calculate total revenue
    sales_summary = df.groupby('region')['revenue'].sum().reset_index()
    # Save to CSV
    sales_summary.to_csv(output_file, index=False)
    print(f"Sales summary saved to {output_file}")

# Example usage
generate_sales_report('sales_data.csv', 'sales_summary.csv')

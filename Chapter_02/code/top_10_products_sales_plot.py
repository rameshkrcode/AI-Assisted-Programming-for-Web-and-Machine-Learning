
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset (ensure it contains 'product' and 'sales' columns)
df = pd.read_csv("sales_data.csv")

# Group by product and calculate total sales
top_products = df.groupby("product")["sales"].sum().nlargest(10)

# Plot the top 10 products by total sales
sns.barplot(x=top_products.values, y=top_products.index)
plt.title("Top 10 Products by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Product")
plt.tight_layout()
plt.show()

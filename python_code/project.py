# sales_analysis.py
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("sales_data.csv") 
print("First 10 rows:")
print(df.head(10))

# Basic summary
print("\nRows, Columns:", df.shape)
print(df.describe(include='all'))

# Total sales by Region
region_sales = df.groupby("Region")["Sales"].sum().reset_index()
print("\nTotal Sales by Region:")
print(region_sales)

# Total sales by Category
category_sales = df.groupby("Category")["Sales"].sum().reset_index()
print("\nTotal Sales by Category:")
print(category_sales)

# Best-selling Products
product_sales = df.groupby("Product")["Sales"].sum().reset_index().sort_values('Sales', ascending=False)
print("\nTop 3 Best-selling Products:")
print(product_sales.head(3))

# --- Visualizations ---

# Bar chart - Sales by Region
plt.figure(figsize=(6,4))
plt.bar(region_sales['Region'], region_sales['Sales'], color='skyblue')
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# Pie chart - Sales by Category
plt.figure(figsize=(5,5))
plt.pie(category_sales['Sales'], labels=category_sales['Category'], autopct='%1.1f%%', startangle=90)
plt.title("Sales Distribution by Category")
plt.show()
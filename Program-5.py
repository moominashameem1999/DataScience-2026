"""Given the list of sales values:
sales = [1200, 3400, 560, 4500, 2100]
Write a Python program to:
1. Print the total sales.
2. Print the average sales.
3. Print the highest sale.
4. Print the lowest sale."""
sales = [1200, 3400, 560, 4500, 2100]
Total_sales = sum(sales)
print(f"Total sales : {Total_sales}")
Average_sales = Total_sales / len(sales)
print(f"Average sales : {Average_sales}")
Highest_sale = max(sales)
print(f"Highest sale : {Highest_sale}")
Lowest_sale = min(sales)
print(f"Lowest sale : {Lowest_sale}")
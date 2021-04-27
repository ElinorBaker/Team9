import csv
with open('sales.csv', 'r') as sales_csv:
    spreadsheet_sales = csv.DictReader(sales_csv)
    for row in spreadsheet_sales:
        print(dict(row))
    sales = []

total_sales = sum(sales)
print('Total Sales: ', total_sales)

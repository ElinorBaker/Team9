import csv
with open('sales.csv', 'r') as sales_csv:
    spreadsheet = csv.DictReader(sales_csv)
    for row in spreadsheet:
        print(dict(row))
#Ideas: total, sales-expenditure, percentage increase/decreaase, average sales/profit, min and max sales/expenditure

#import csv
#with open('sales.csv', 'r') as sales_csv:
    #spreadsheet_sales = csv.DictReader(sales_csv)
    #for row in spreadsheet_sales:
     #   print(dict(row))
    #sales = []

#total_sales = sum(sales)
#print('Total Sales: ', total_sales)

sales_list = [6226, 1521, 1842, 2051, 1728, 2138, 7479, 4434, 3615, 5472, 7224, 1812]
total_sales = sum(sales_list)
print(total_sales)
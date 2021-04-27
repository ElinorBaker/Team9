#Ideas: total, sales-expenditure, percentage increase/decreaase, average sales/profit, min and max sales/expenditure

#import csv
#with open('sales.csv', 'r') as sales_csv:
    #spreadsheet_sales = csv.DictReader(sales_csv)
    #for row in spreadsheet_sales:
     #   print(dict(row))
    #sales = []

#total_sales = sum(sales)
#print('Total Sales: ', total_sales)

monthly_profit = input('Which month would you like to see the profit of?').upper()
jan_profit = jan_sales - jau_expenditure
feb_profit = feb_sales - feb_expenditure
mar_profit = mar_sales - mar_expenditure
apr_profit = apr_sales - apr_expenditure
may_profit = may_sales - may_expenditure

if monthly_profit == 'JANUARY':
    print('Total January Profit: ', jan_profit)
elif monthly_profit == 'FEBRUARY':
    print('Total February Profit: ', feb_profit)
elif monthly_profit == 'MARCH':
    print('Total March Profit: ', mar_profit)
elif monthly_profit == 'APRIL':
    print('Total April Profit: ', apr_profit)
elif monthly_profit == 'MAY':
    print('Total May Profit: ', may_profit)
elif monthly_profit == 'JUNE':
    print('Total June Profit: ', jun_profit)
elif monthly_profit == 'JULY':
    print('Total July Profit: ', jul_profit)
elif monthly_profit == 'AUGUST':
    print('Total August Profit: ', aug_profit)
elif monthly_profit == 'SEPTEMBER':
    print('Total September Profit: ', sept_profit)
elif monthly_profit == 'OCTOBER':
    print('Total October Profit: ', oct_profit)
elif monthly_profit == 'NOVEMBER':
    print('Total November Profit: ', nov_profit)
elif monthly_profit == 'DECEMBER':
    print('Total December Profit: ', dec_profit)


sales_list = [6226, 1521, 1842, 2051, 1728, 2138, 7479, 4434, 3615, 5472, 7224, 1812]
total_sales = sum(sales_list)
print(total_sales)
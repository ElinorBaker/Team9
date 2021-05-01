#Ideas: total, sales-expenditure, percentage increase/decreaase, average sales/profit, min and max sales/expenditure

import csv
with open('sales.csv', 'r') as sales_csv:
    spreadsheet_sales = csv.DictReader(sales_csv)
    for row in spreadsheet_sales:
        print(dict(row))
    sales = []

jan_sales = 6226
feb_sales = 1521
mar_sales = 1842
apr_sales = 2051
may_sales = 1728
jun_sales = 2138
jul_sales = 7479
aug_sales = 4434
sep_sales = 3615
oct_sales = 5472
nov_sales = 7224
dec_sales = 1812

jan_expend = 3808
feb_expend = 3373
mar_expend = 3965
apr_expend = 1098
may_expend = 3046
jun_expend = 2258
jul_expend = 2084
aug_expend = 2799
sep_expend = 1649
oct_expend = 1116
nov_expend = 1431
dec_expend = 3532

monthly_profit = input('Which month would you like to see the profit of?').upper()
jan_prof = jan_sales - jan_expend
feb_prof = feb_sales - feb_expend
mar_prof = mar_sales - mar_expend
apr_prof = apr_sales - apr_expend
may_prof = may_sales - may_expend
jun_prof = jun_sales - jun_expend
jul_prof = jul_sales - jul_expend
aug_prof = aug_sales - aug_expend
sep_prof = sep_sales - sep_expend
oct_prof = oct_sales - oct_expend
nov_prof = nov_sales - nov_expend
dec_prof = dec_sales - dec_expend

if monthly_profit == 'JANUARY':
    print('Total January Profit: ', jan_prof)
elif monthly_profit == 'FEBRUARY':
    print('Total February Profit: ', feb_prof)
elif monthly_profit == 'MARCH':
    print('Total March Profit: ', mar_prof)
elif monthly_profit == 'APRIL':
    print('Total April Profit: ', apr_prof)
elif monthly_profit == 'MAY':
    print('Total May Profit: ', may_prof)
elif monthly_profit == 'JUNE':
    print('Total June Profit: ', jun_prof)
elif monthly_profit == 'JULY':
    print('Total July Profit: ', jul_prof)
elif monthly_profit == 'AUGUST':
    print('Total August Profit: ', aug_prof)
elif monthly_profit == 'SEPTEMBER':
    print('Total September Profit: ', sep_prof)
elif monthly_profit == 'OCTOBER':
    print('Total October Profit: ', oct_prof)
elif monthly_profit == 'NOVEMBER':
    print('Total November Profit: ', nov_prof)
elif monthly_profit == 'DECEMBER':
    print('Total December Profit: ', dec_prof)

sales_list = [6226, 1521, 1842, 2051, 1728, 2138, 7479, 4434, 3615, 5472, 7224, 1812]
total_sales = sum(sales_list)

overall_sales = input('Would you like to see the total profits? y/n')
if overall_sales == "y":
   print(total_sales)
elif overall_sales:
   print("No problem, stats is boring anyway!!!")
# 1 IMPORT SECTION:
# 1.1 CSV
import csv
with open('sales.csv', 'r') as sales_csv:
    spreadsheet_sales = csv.DictReader(sales_csv)
    sales = []
    for row in spreadsheet_sales:
        sales.append(dict(row))

# 1.2 FUNCTIONS
from function_library import another_stat
from function_library import another_month

def average(av):
    avg = sum(av)/len(av)
    return avg

# 2 QUESTIONS SECTION:
print("WELCOME TO THE ANNUAL SALES REVIEW!")
while True:
    option = input('MAIN MENU: Would you like to see statistics for SALES, EXPENDITURES, or PROFIT? (S/E/P)').upper()

    # 2.1 QUESTIONS ABOUT SALES
    if option == "S":
        done = False
        while not done:
            sales_section = input('SALES MENU: Would you like to see the sales BY MONTH(1), YEARLY TOTAL(2), YEARLY AVERAGE(3) or MIN/MAX?(4)? (1/2/3/4)')

            # 2.1.2 Monthly Sales
            if sales_section == "1":
                month_check = False
                while not month_check:
                    monthly_user_input = input('Which month would you like to see the sales of? (1/2/3 etc.)')
                    if monthly_user_input in ['1','2','3','4','5','6','7','8','9','10','11','12']:
                        # OR didn't work, so used in []
                        monthly_sales = [int(row['sales']) for row in sales if row['month_no'] == monthly_user_input]
                        corresponding_month = [row['month_name'] for row in sales if row['month_no'] == monthly_user_input]
                        print("The sales for {} was {}.".format(str(corresponding_month)[2:-2], str(monthly_sales)[1:-1]))
                        # Fixed cosmetic issue of [''] list output.
                        month_check = another_month()
                    else:
                        print('Invalid response. Please try again.')

            # 2.1.2 Total Sales
            if sales_section == "2":
                total_sales = sum([int(row['sales']) for row in sales])
                print('The total sales for this year was {}.'.format(str(total_sales)))
                done = another_stat()

            # 2.1.3 Average Sales
            elif sales_section == "3":
                average_sales = round(average([int(row['sales']) for row in sales]), 2)
                print("This year's average sales was {}.".format(str(average_sales)))
                done = another_stat()

            # 2.1.4 Min/Max Sales
            elif sales_section == "4":
                show_minmax_sales = input('Would you like to see the HIGHEST or LOWEST monthly sales? (H/L)').upper()
                max_sales = max([int(row['sales']) for row in sales])
                max_sales_month = [row['month_name'] for row in sales if row['sales'] == str(max_sales)]
                min_sales = min([int(row['sales']) for row in sales])
                min_sales_month = [row['month_name'] for row in sales if row['sales'] == str(min_sales)]
                if show_minmax_sales == 'H':
                    print('The highest monthly sales was {}, from {}.'.format(str(max_sales), str(max_sales_month)[2:-2]))
                    done = another_stat()
                elif show_minmax_sales == 'L':
                    print('The lowest monthly sales was {}, from {}.'.format(str(min_sales), str(min_sales_month)[2:-2]))
                    done = another_stat()
                else:
                    print('Invalid response! Returning to SALES MENU.')
                    # Ideally would have gone back to 'show_minmax_sales' but we made it work!

    # 2.2 QUESTIONS ABOUT EXPENDITURE
    elif option == "E":
        done = False
        while not done:
            expend_section = input('EXPENDITURE MENU: Would you like to see the expenditure BY MONTH(1), YEARLY TOTAL(2), YEARLY AVERAGE(3) or MIN/MAX?(4)? (1/2/3/4)')

            # 2.2.1 Monthly Expenditure
            if expend_section == "1":
                month_check = False
                while not month_check:
                    monthly_user_input = input('Which month would you like to see the expenditure of? (1/2/3 etc.)')
                    if monthly_user_input in ['1','2','3','4','5','6','7','8','9','10','11','12']:
                        monthly_expend = [int(row['expenditure']) for row in sales if row['month_no'] == monthly_user_input]
                        corresponding_month = [row['month_name'] for row in sales if row['month_no'] == monthly_user_input]
                        print("The expenditure for {} was {}.".format(str(corresponding_month)[2:-2], str(monthly_expend)[1:-1]))
                        month_check = another_month()
                    else:
                        print('Invalid response. Please try again.')

            # 2.2.2 Total Expenditure
            if expend_section == "2":
                total_expend = sum([int(row['expenditure']) for row in sales])
                print("This year's total expenditure was {}.".format(str(total_expend)))
                done = another_stat()

            # 2.2.3 Average Expenditure
            if expend_section == "3":
                average_expend = round(average([int(row['expenditure']) for row in sales]), 2)
                print("The average expenditure this year was {}.".format(str(average_expend)))
                done = another_stat()

            # 2.2.4 Min/Max Expenditure
            if expend_section == "4":
                show_minmax_expand = input('Would you like to see the HIGHEST or LOWEST monthly expenditure? (H/L)').upper()
                max_expend = max([int(row['expenditure']) for row in sales])
                max_expend_month = [row['month_name'] for row in sales if row['expenditure'] == str(max_expend)]
                min_expend = min([int(row['expenditure']) for row in sales])
                min_expend_month = [row['month_name'] for row in sales if row['expenditure'] == str(min_expend)]
                if show_minmax_expand == 'H':
                    print('The highest monthly expenditure was {}, from {}.'.format(str(max_expend), str(max_expend_month)[2:-2]))
                    done = another_stat()
                elif show_minmax_expand == 'L':
                    print('The lowest monthly expenditure was {}, from {}.'.format(str(min_expend), str(min_expend_month)[2:-2]))
                    done = another_stat()
                else:
                    print('Invalid response! Returning to EXPENDITURE MENU.')

    # 2.3 QUESTIONS ABOUT PROFIT
    elif option == "P":
        done = False
        while not done:
            profit_section = input('PROFIT MENU: Would you like to see the profits BY MONTH(1), YEARLY TOTAL(2), YEARLY AVERAGE(3) or MIN/MAX?(4)?')

            # 2.3.1 Profit Per Month
            if profit_section == "1":
                month_check = False
                while not month_check:
                    monthly_user_input = input('Which month would you like to see the profits of? (1/2/3 etc.)')
                    if monthly_user_input in ['1','2','3','4','5','6','7','8','9','10','11','12']:
                        # Failed to make monthly_profit an integer, so used sum() to do it.
                        monthly_profit = sum([int(row['profit']) for row in sales if row['month_no'] == monthly_user_input])
                        corresponding_month = [row['month_name'] for row in sales if row['month_no'] == monthly_user_input]
                        if monthly_profit > 0:
                            print("The profit for {} was {}.".format(str(corresponding_month)[2:-2], str(monthly_profit)))
                        elif monthly_profit < 0:
                            print("The deficit for {} was {}.".format(str(corresponding_month)[2:-2], str(monthly_profit)))
                        month_check = another_month()
                    else:
                        print('Invalid response. Please try again.')

            # 2.3.2 Total Profit
            elif profit_section == "2":
                total_sales = sum([int(row['sales']) for row in sales])
                total_expend = sum([int(row['expenditure']) for row in sales])
                total_profit = total_sales - total_expend
                print("The total profit for this year was {}.".format(str(total_profit)))
                done = another_stat()

            # 2.3.3 Average Profit
            elif profit_section == "3":
                average_profit = round(sum([int(row['profit']) for row in sales])/7, 2)
                print("This year's average profit was {}.".format(str(average_profit)))
                done = another_stat()

            # 2.3.4 Min/Max Profit
            elif profit_section == "4":
                show_minmax_profit = input('Would you like to see the HIGHEST or LOWEST monthly profit? (H/L)').upper()
                max_profit = max([int(row['profit']) for row in sales])
                max_profit_month = [row['month_name'] for row in sales if row['profit'] == str(max_profit)]
                min_profit = min([int(row['profit']) for row in sales])
                min_profit_month = [row['month_name'] for row in sales if row['profit'] == str(min_profit)]
                if show_minmax_profit == 'H':
                    print('The highest monthly profit was {}, from {}.'.format(str(max_profit), str(max_profit_month)[2:-2]))
                    done = another_stat()
                elif show_minmax_profit == 'L':
                    print('The lowest monthly profit was a deficit of {}, from {}.'.format(str(min_profit), str(min_profit_month)[2:-2]))
                    done = another_stat()
                else:
                    print('Invalid response! Returning to PROFIT MENU.')

    else:
        stats_loop = input("Sorry, invalid response. Would you like to try again? (Y/N)").upper()
        if stats_loop == "N":
            print("Goodbye!")
            exit()
        elif stats_loop == "Y":
            continue

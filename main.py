# Issues: How to get out of nested loops??? Figure "Would you like to see another statistic?" out
# In-Progress: Section 2.3.1 (Work out see another month loop)
# Minor Issues: Invalid responses, currently solved by 'While True' looping indefinitely until expected response recieved.

# 1 RAW DATA SECTION:
'''
import csv
with open('sales.csv', 'r') as sales_csv:
    spreadsheet_sales = csv.DictReader(sales_csv)
    for row in spreadsheet_sales:
        print(dict(row))
    sales = []
'''

from statistics import mean
def average(l):
    avg= sum(l)/len(l)
    return avg

# 1.1 RAW DATA - SALES
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
max_sales_month = 'July'
min_sales_month = 'February'

sales_list = [6226, 1521, 1842, 2051, 1728, 2138, 7479, 4434, 3615, 5472, 7224, 1812]
total_sales = sum(sales_list)
max_sales = max(sales_list)
min_sales = min(sales_list)
sales_average = round(average(sales_list), 2)

# 1.2 RAW DATA - EXPENDITURES
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
max_expend_month = 'January'
min_expend_month = 'April'

expend_list = [3808, 3373, 3965, 1098, 3046, 2258, 2084, 2799, 1649, 1116, 1431, 3532]
total_expend = sum(expend_list)
max_expend = max(expend_list)
min_expend = min(expend_list)
expend_average = round(average(expend_list), 2)

# 1.3 RAW DATA - PROFIT
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

profit_list = [jan_prof, feb_prof, mar_prof, apr_prof, may_prof, jun_prof, jul_prof, aug_prof, sep_prof, oct_prof, nov_prof, dec_prof]
max_profit_month = 'November'
min_profit_month = 'March'
total_prof = sum(profit_list)
max_profit = max(profit_list)
min_profit = min(profit_list)
profit_average = round(average(profit_list), 2)

# 2 QUESTIONS SECTION:
print("WELCOME TO THE ANNUAL SALES REVIEW!")
while True:
    option = input ('Would you like to see statistics for SALES, EXPENDITURES, or PROFIT? (S/E/P)').upper()

    # 2.1 QUESTIONS ABOUT SALES
    if option == "S":
        while True:
            sales_section = input('Would you like to see the sales YEARLY TOTAL(1), YEARLY AVERAGE(2) or MIN/MAX?(3)? (1/2/3)')

            # 2.1.1 Total Sales
            if sales_section == "1":
                overall_sales = input('Please confirm: see total sales? (Y/N)').upper()
                if overall_sales == "Y":
                    print('The total sales for this year was {}.'.format(total_sales))
                    top_loop_question = input("Would you like to see another statistic? (Y/N)").upper()
                    if top_loop_question != "Y":
                        print("Goodbye!")
                        exit()
                    elif top_loop_question == "N":
                            break # HOW TO GET TO OUTERMOST LOOP??
                    elif overall_sales == "N":
                        print("No problem! Stats is boring anyway!!!")
                        top_loop_question = input("Would you like to see another statistic? (Y/N)").upper()
                        if top_loop_question != "Y":
                            print("Goodbye!")
                            exit()
                        elif top_loop_question == "N":
                            break # HOW TO GET TO OUTERMOST LOOP??

            # 2.1.2 Average Sales
            elif sales_section == "2":
                show_averagesales = input('Please confirm: see average yearly sales? (Y/N)').upper()
                if show_averagesales == "Y":
                    print("This year's average sales was {}.".format(sales_average))
                    top_loop_question = input("Would you like to see another statistic? (Y/N)").upper()
                    if top_loop_question != "Y":
                        print("Goodbye!")
                        exit()
                    elif top_loop_question == "N":
                        break  # HOW TO GET TO OUTERMOST LOOP??
                elif show_averagesales == "N":
                    print('Whatever then, suit yourself...')
                    top_loop_question = input("Would you like to see another statistic? (Y/N)").upper()
                    if top_loop_question != "Y":
                        print("Goodbye!")
                        exit()
                    elif top_loop_question == "N":
                        break  # HOW TO GET TO OUTERMOST LOOP??

            # 2.1.3 Min/Max Sales
            elif sales_section == "3":
                show_minmax_sales = input('Would you like to see the HIGHEST or LOWEST monthly sales? (H/L)').upper()
                if show_minmax_sales == 'H':
                    print('The highest monthly sales was {}, from {}.'.format(max_sales, max_sales_month))
                    top_loop_question = input("Would you like to see another statistic? (Y/N)").upper()
                    if top_loop_question != "Y":
                        print("Goodbye!")
                        exit()
                    elif top_loop_question == "N":
                        break  # HOW TO GET TO OUTERMOST LOOP??
                elif show_minmax_sales == 'L':
                    print('The lowest monthly sales was {}, from {}.'.format(min_sales, min_sales_month))
                    top_loop_question = input("Would you like to see another statistic? (Y/N)").upper()
                    if top_loop_question != "Y":
                        print("Goodbye!")
                        exit()
                    elif top_loop_question == "N":
                        break  # HOW TO GET TO OUTERMOST LOOP??

    # 2.2 QUESTIONS ABOUT EXPENDITURE
    elif option == "E":
        while True:
            expend_section = input('Would you like to see the expenditure YEARLY TOTAL(1), YEARLY AVERAGE(2) or MIN/MAX?(3)? (1/2/3)')

            # 2.2.1 Total Expenditure
            if expend_section == "1":
                overall_expend = input('Please confirm: see total expenditure? (Y/N)').upper()
                if overall_expend == "Y":
                    print("This year's total expenditure was {}.".format(total_expend))
                    top_loop_question = input("Would you like to see another statistic? (Y/N)").upper()
                    if top_loop_question != "Y":
                        print("Goodbye!")
                        exit()
                    elif top_loop_question == "N":
                        break  # HOW TO GET TO OUTERMOST LOOP??
                elif overall_expend == "N":
                    print('Like I said, stats is boring anyway lol.')
                    top_loop_question = input("Would you like to see another statistic? (Y/N)").upper()
                    if top_loop_question != "Y":
                        print("Goodbye!")
                        exit()
                    elif top_loop_question == "N":
                        break  # HOW TO GET TO OUTERMOST LOOP??

            # 2.2.2 Average Expenditure
            if expend_section == "2":
                show_averageexpend = input('Please confirm: see average expenditure? (Y/N)').upper()
                if show_averageexpend == "Y":
                    print("The average expenditure this year was {}.".format(expend_average))
                    top_loop_question = input("Would you like to see another statistic? (Y/N)").upper()
                    if top_loop_question != "Y":
                        print("Goodbye!")
                        exit()
                    elif top_loop_question == "N":
                        break  # HOW TO GET TO OUTERMOST LOOP??
                elif show_averageexpend == "N":
                    print('Whatever then, suit yourself...')
                    top_loop_question = input("Would you like to see another statistic? (Y/N)").upper()
                    if top_loop_question != "Y":
                        print("Goodbye!")
                        exit()
                    elif top_loop_question == "N":
                        break  # HOW TO GET TO OUTERMOST LOOP??

            # 2.2.2 Min/Max Expenditure
            if expend_section == "3":
                show_minmax_expand = input('Would you like to see the HIGHEST or LOWEST monthly expenditure? (H/L)').upper()
                if show_minmax_expand == 'H':
                    print('The highest monthly expenditure was {}, from {}.'.format(max_expend, max_expend_month))
                    top_loop_question = input("Would you like to see another statistic? (Y/N)").upper()
                    if top_loop_question != "Y":
                        print("Goodbye!")
                        exit()
                    elif top_loop_question == "N":
                        break  # HOW TO GET TO OUTERMOST LOOP??
                elif show_minmax_expand == 'L':
                    print('The lowest monthly expenditure was {}, from {}.'.format(min_expend, min_expend_month))
                    top_loop_question = input("Would you like to see another statistic? (Y/N)").upper()
                    if top_loop_question != "Y":
                        print("Goodbye!")
                        exit()
                    elif top_loop_question == "N":
                        break  # HOW TO GET TO OUTERMOST LOOP??

    # 2.3 QUESTIONS ABOUT PROFIT
    elif option == "P":
        while True:
            profit_section = input('Would you like to see the profits BY MONTH(1), YEARLY TOTAL(2), YEARLY AVERAGE(3) or MIN/MAX?(4)?')

            # 2.3.1 Profit Per Month
            if profit_section == "1":
                while True:
                    monthly_profit = input('Which month would you like to see the profit of? (1/2/3 etc.)')
                    if monthly_profit == '1':
                        print('Total January Profit:', jan_prof)
                        month_loop_question = input("Would you like to see another month's profit? (Y/N)").upper()
                        if month_loop_question != "Y":
                            top_loop_question = input("Would you like to see another statistic? (Y/N)").upper()
                            if top_loop_question != "Y":
                                print("Goodbye!")
                                exit()
                            elif top_loop_question == "N":
                                break #HOW TO GET TO OUTERMOST LOOP??
                        elif month_loop_question == "N":
                            continue
                    elif monthly_profit == '2':
                        print('Total February Profit:', feb_prof)
                    elif monthly_profit == '3':
                        print('Total March Profit:', mar_prof)
                    elif monthly_profit == '4':
                        print('Total April Profit:', apr_prof)
                    elif monthly_profit == '5':
                        print('Total May Profit:', may_prof)
                    elif monthly_profit == '6':
                        print('Total June Profit:', jun_prof)
                    elif monthly_profit == '7':
                        print('Total July Profit:', jul_prof)
                    elif monthly_profit == '8':
                        print('Total August Profit:', aug_prof)
                    elif monthly_profit == '9':
                        print('Total September Profit:', sep_prof)
                    elif monthly_profit == '10':
                        print('Total October Profit:', oct_prof)
                    elif monthly_profit == '11':
                        print('Total November Profit:', nov_prof)
                    elif monthly_profit == '12':
                        print('Total December Profit:', dec_prof)

            # 2.3.1 Total Profit
            elif profit_section == "2":
                overall_profit = input('Please confirm: see total profits for the year? (Y/N)').upper()
                if overall_profit == "Y":
                    print("The total profit for this year was {}.".format(total_prof))
                    top_loop_question = input("Would you like to see another statistic? (Y/N)").upper()
                    if top_loop_question != "Y":
                        print("Goodbye!")
                        exit()
                    elif top_loop_question == "N":
                        break  # HOW TO GET TO OUTERMOST LOOP??
                elif overall_profit == "N":
                    print("Eh who needs to know they've made any money anyway!")
                    top_loop_question = input("Would you like to see another statistic? (Y/N)").upper()
                    if top_loop_question != "Y":
                        print("Goodbye!")
                        exit()
                    elif top_loop_question == "N":
                        break  # HOW TO GET TO OUTERMOST LOOP??

            # 2.3.3 Average Profit
            elif profit_section == "3":
                show_averageprofit = input('Please confirm: see yearly average profit? (Y/N)').upper()
                if show_averageprofit == "Y":
                    print("This year's average profit was {}.".format(profit_average))
                elif show_averageprofit == "N":
                    print('Whatever then, suit yourself...')
                    top_loop_question = input("Would you like to see another statistic? (Y/N)").upper()
                    if top_loop_question != "Y":
                        print("Goodbye!")
                        exit()
                    elif top_loop_question == "N":
                        break  # HOW TO GET TO OUTERMOST LOOP??

            # 2.3.4 Min/Max Profit
            elif profit_section == "4":
                show_minmax_profit = input('Would you like to see the HIGHEST or LOWEST monthly profit? (H/L)').upper()
                if show_minmax_profit == 'H':
                    print('The highest monthly profit was {}, from {}.'.format(max_profit, max_profit_month))
                    top_loop_question = input("Would you like to see another statistic? (Y/N)").upper()
                    if top_loop_question != "Y":
                        print("Goodbye!")
                        exit()
                    elif top_loop_question == "N":
                        break  # HOW TO GET TO OUTERMOST LOOP??
                if show_minmax_profit == 'L':
                    print('The lowest monthly profit was a defecit of {}, from {}.'.format(min_profit, min_profit_month))
                    top_loop_question = input("Would you like to see another statistic? (Y/N)").upper()
                    if top_loop_question != "Y":
                        print("Goodbye!")
                        exit()
                    elif top_loop_question == "N":
                        break  # HOW TO GET TO OUTERMOST LOOP??

    else:
        print("Sorry, invalid response. Please try again!")
        stats_loop = input("Would you like to try again? (Y/N)").upper()
        if stats_loop != "Y": # Why does Y/N seem to be reversed?
            print("Goodbye!")
            exit()
        elif stats_loop == "N":
            continue



# INACTIVE CODE BELOW
'''
# 2.1 QUESTIONS ABOUT SALES
# 2.1.1 Total Sales
overall_sales = input('Would you like to see the total sales? (Y/N)').upper()
if overall_sales == "Y":
   print('The total sales for this year was {}.'.format(total_sales))
elif overall_sales:
   print("No problem! Stats is boring anyway!!!")

# 2.1.2 Average Sales
show_averagesales = input('Would you like to see the average yearly sales? (Y/N)').upper()
if show_averagesales == "Y":
    print("This year's average sales was {}.".format(sales_average))
elif show_averagesales:
    print('Whatever then, suit yourself...')

# 2.1.3 Min/Max Sales
show_minmax_sales = input('Would you like to see the HIGHEST or LOWEST monthly sales? (H/L)').upper()
if show_minmax_sales == 'H':
    print('The highest monthly sales was {}, from {}.'.format(max_sales, max_sales_month))
elif show_minmax_sales == 'L':
    print('The lowest monthly sales was {}, from {}.'.format(min_sales, min_sales_month))

# 2.2 QUESTIONS ABOUT EXPENDITURE
# 2.2.1 Total Expenditure
overall_expend = input('Would you like to see the total expenditure? (Y/N)').upper()
if overall_expend == "Y":
    print("This year's total expenditure was {}.".format(total_expend))
elif overall_expend:
    print('Like I said, stats is boring anyway lol.')

# 2.2.2 Average Expenditure
show_averageexpend = input('Would you like to see the average expenditure? (Y/N)').upper()
if show_averageexpend == "Y":
    print("The average expenditure this year was {}.".format(expend_average))
elif show_averageexpend:
    print('Whatever then, suit yourself...')

# 2.2.2 Min/Max Expenditure
show_minmax_expand = input('Would you like to see the HIGHEST or LOWEST monthly expenditure? (H/L)').upper()
if show_minmax_expand == 'H':
    print('The highest monthly expenditure was {}, from {}.'.format(max_expend, max_expend_month))
elif show_minmax_expand == 'L':
    print('The lowest monthly expenditure was {}, from {}.'.format(min_expend, min_expend_month))

# 2.3 QUESTIONS ABOUT PROFIT
# 2.3.1 Total Profit
overall_prof = input('Would you like to see the total profits for the year? (Y/N)')
if overall_prof == "Y":
    print("The total profit for this year was {}.".format(total_prof))
elif overall_prof:
    print("Eh who needs to know they've made any money anyway!")

# 2.3.2 Average Profit
show_averageprofit = input('Would you like to see the average profit? (Y/N)').upper()
if show_averagesales == "Y":
    print("This year's average profit was {}.".format(profit_average))
elif show_averageprofit:
    print('Whatever then, suit yourself...')

# 2.3.3 Min/Max Profit
show_minmax_profit = input('Would you like to see the HIGHEST or LOWEST monthly profit? (H/L)').upper()
if show_minmax_profit == 'H':
    print('The highest monthly profit was {}, from {}.'.format(max_profit, max_profit_month))
elif show_minmax_profit == 'L':
    print('The lowest monthly profit was a defecit of {}, from {}.'.format(min_profit, min_profit_month))

# 2.3.4 Profit Per Month
monthly_profit = input('Which month would you like to see the profit of? (1/2/3 etc.)')
if monthly_profit == '1':
    print('Total January Profit:', jan_prof)
elif monthly_profit == '2':
    print('Total February Profit:', feb_prof)
elif monthly_profit == '3':
    print('Total March Profit:', mar_prof)
elif monthly_profit == '4':
    print('Total April Profit:', apr_prof)
elif monthly_profit == '5':
    print('Total May Profit:', may_prof)
elif monthly_profit == '6':
    print('Total June Profit:', jun_prof)
elif monthly_profit == '7':
    print('Total July Profit:', jul_prof)
elif monthly_profit == '8':
    print('Total August Profit:', aug_prof)
elif monthly_profit == '9':
    print('Total September Profit:', sep_prof)
elif monthly_profit == '10':
    print('Total October Profit:', oct_prof)
elif monthly_profit == '11':
    print('Total November Profit:', nov_prof)
elif monthly_profit == '12':
    print('Total December Profit:', dec_prof)
'''








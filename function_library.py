def another_stat():
        top_loop_question = input("Would you like to see another statistic? (Y/N)").upper()
        if top_loop_question == "N":
            print("Goodbye!")
            exit()
        return top_loop_question == "Y"

def another_month():
    another_month_question = input("Would you like to see the statistics for another month? (Y/N)").upper()
    if another_month_question == "N":
        print("Goodbye!")
        exit()
    return another_month_question == "Y"


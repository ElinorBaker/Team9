# Function 1: go back to MAIN MENU
def another_stat():
        top_loop_question = input("Would you like to go back to the MAIN MENU? (Y/N)").upper()
        if top_loop_question == "N":
            print("Goodbye!")
            exit()
        elif top_loop_question != "Y" or "N":
            print('Invalid response. Transferring you back to the MAIN MENU.')
            return top_loop_question
        return top_loop_question == "Y"

# Function 2: another month?
def another_month():
    another_month_question = input("Would you like to see this statistic for another month? (Y/N)").upper()
    if another_month_question == "N":
        print("Goodbye!")
        exit()
    elif another_month_question == "Y":
       return

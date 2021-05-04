# Function 1: average
def average(av):
    avg = sum(av)/len(av)
    return avg

# Function 2: go back to MAIN MENU
def another_stat():
        top_loop_question = input("Would you like to go back to the MAIN MENU to see another statistic? (Y/N)").upper()
        if top_loop_question == "N":
            print("Goodbye!")
            exit()
        elif top_loop_question not in ["Y", "N"]:
            print('Invalid response. Transferring you back to the MAIN MENU.')
            return top_loop_question
        return top_loop_question == "Y"

# Function 3: another month
def another_month():
    another_month_question = input("Would you like to see this statistic for another month? (Y/N)").upper()
    if another_month_question == "N":
        print("Goodbye!")
        exit()
        # Ideally instead of exit() would be function another_stat(), but nested loop 'return' does not go where expected...
    elif another_month_question == "Y":
       return

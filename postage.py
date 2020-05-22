"""
File: postage.py
-------------------------
This program is a tool to help you calculate the cost of postage for
First-Class letters within the USA.
"""

from intro import *
from check_size import *
from weight import *
from cost import *


"""
Main Function:
1. Create an empty dictionary called 'item' to store key-value pairs for the item being mailed out.
2. Print introduction - introduction()
3. Retrieve type of item - check_item()
    a. If the item is a postcard: console prints cost of mailing the card/how many stamps to use, then end
    b. If it's not a postcard, it checks if it's a standard, irregular, or large envelope
4. If the size is NOT a postcard, continue executing the following:
    a. Take weight of item
    b. Calculate cost of shipping item
    c. Print cost of shipping item
"""


def main():
    # will hold key-value pairs of the item being mailed.
    item = {}
    # will continue running as long as the loop is True.
    run_loop = True

    introduction()
    while run_loop:
        check_item(item)

        if item['type'] == "postcard" or item['type'] == "parcel":
            run_loop = run_program(item)
        # move onto checking weight and cost of item if it's NOT a postcard and NOT parcel
        elif not item['type'] == "postcard" and not item['type'] == "parcel":
            weight(item)
            calculate_cost(item)
            print_cost(item)
            run_loop = run_program(item)


#################################### HELPER FUNCTIONS ####################################


# this function keeps the program running as long as user wants to check another item.
def run_program(item):
    print("")
    print("Do you want to check the cost of another item? 😅")
    check_another_item = input('Please enter "yes" or "no": ')

    # if user wants to check another item, run this code
    if check_another_item.lower() == "yes":
        print("")
        print("Great! Let's check another item.")
        # erases all information about item to check a new item
        item.clear()
        # keeps loop going
        return True

    # if not, end the program
    elif check_another_item.lower() == "no" or check_another_item.lower() == "exit":
        print("")
        print("Thanks for using Postage Calculator! 🥳")
        # ends loop
        return False

    # catches input errors
    elif not check_another_item.lower() == "yes" and not check_another_item.lower() == "no":
        print("")
        print("Sorry, that's not a valid answer. Try again.")
        return run_program(item)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()

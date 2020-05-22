"""
### weight() ###
This function will check the weight of the item, then print the cost of mailing the item.
1) Accept weight from user in ounces.
    a) Attempt to convert the input into a float, provided that the number is a positive number.
    b) Save float to item['weight'].
2) If item['type'] is standard or irregular, check that the weight is not more than 3.5 ounces.
    All packages that are more than 3.5 oz must be mailed as a large envelope, not a standard/irregular envelope.
    a) check_heavy_reg_envelope checks if item['weight'] is heavier than 3.5 oz.
    b) If it's heavier than 3.5 oz, update item['type'] to large
"""

from constants import exitable_input


# main function to check weight and cost
def weight(item):
    item['weight'] = take_weight()

    # check if it's too heavy to send as standard/irregular envelope
    # if it's heavier than 3.5 oz, we'll update the item['type'] to be large instead.
    if item['type'] == "standard" or item['type'] == "irregular":
        check_heavy_reg_envelope(item)

    # check if it's too heavy to send as large envelope
    # if it's heavier than 13 oz, update item['type'] to be parcel and don't calculate cost
    elif item['type'] == 'large':
        check_heavy_lrg_envelope(item)


#################################### HELPER FUNCTIONS ####################################


# will calculate the cost of postage
def take_weight():
    # prompt user for weight
    print("")
    str_weight = exitable_input("Please input the weight of your envelope in ounces. "
                                '(For example, if your envelope weighs 1.2 ounces, enter "1.2"): ')

    # this will try to convert the entered in weight into a float.
    try:
        flt_weight = float(str_weight)

        while flt_weight < 0:  # if not a positive num, print message and ask for input again
            print("Sorry, input must be a positive number, try again.")
            # recursion
            return take_weight()

        # if it's a positive number, we can return the weight.
        return flt_weight

    # this produces a ValueError if user enters something that can't be converted to a float.
    except ValueError:
        print("")
        print("Sorry, that's not a valid answer. Try again.")
        # recursion to prompt user to enter a valid number.
        return take_weight()


# this function changes the envelope_type of a standard envelope to large if weight is above 3.5 oz.
def check_heavy_reg_envelope(item):
    if item['weight'] > 3.5:
        print("")
        print("Oops! Your package is over 3.5 oz! 😱 "
              "That means you'll have to mail it as a LARGE envelope.")
        print("Don't worry -- we'll calculate the cost for you!")
        item['type'] = "large"


# this function changes item['type'] of a large envelope to parcel if weight is above 13 oz.
def check_heavy_lrg_envelope(item):
    if item['weight'] > 13:
        print("")
        print('Sorry, your package is too large to be mailed as a letter. 😭')
        print('Please take it to your local USPS store and have it delivered as a parcel. 📦')
        item['type'] = 'parcel'

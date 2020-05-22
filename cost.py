"""
### calculate_cost() ###
This function will calculate and print the cost of mailing our item.
1) First, it checks the item['type'].
    a) If item['type'] is 'standard' or 'irregular', calculate using standard postage pricing.
    b) If item['type'] is 'large', calculate using large postage pricing.
2) From there, write two helper functions: one to calculate standard pricing, another to calculate large pricing
    a) For standard pricing:
        1. Base postage cost should be a FOREVER stamp, which we save as a constant. This makes it easier to update
            the cost of the stamp as prices increase over time.
        2. Initialize item['cost'] to be the base postage cost.
        3. Additionally, initialize item['add_oz'] to be 0. item['add_oz'] will track the number of additional
            ounce stamps needed to mail our item.
        4. If the weight is less than or equal to 1 oz, the postage price will remain as the item['cost'], as
            no additional ounce stamps will be needed. (One FOREVER stamp covers mail <= 1 oz.)
        5. If it's more than 1 oz and less than or equal to 3.5 oz, write a for loop with a range from 2-5 that:
            a. Update item['cost'] = base_postage + (ADDITIONAL_OZ * (i - 1))
            b. Update item['add_oz'] = i - 1
            c. Add a break so that the loop doesn't continue once the condition is met
            * Note: Our range is 2-5 because we want the loop to end before 5. (Max weight for standard envelope is 3.5.)
        6. If item['type'] is 'irregular', we have to add the 15¢ surcharge to item['cost'] and increase item['add_oz']
            by 1 (irregular items always have a 15¢ surcharge that can be covered by an add. oz stamp.)
    b) For large pricing:
        1. Base postage cost is LARGE_ENVELOPE_BASE, saved as a constant. This makes it easier to update the cost of
            the stamp as prices increase over time.
        2. Initialize item['cost'] to the base postage cost.
        3. If weight is less than or equal to 1 oz, the postage price will remain as the item['cost'].
        4. If weight is more than 1 oz and less than or equal to 13 oz, write a for loop with a range from 2-14 that
            adds LARGE_ENVELOPE_ADD_OZ for every additional 1 ounce.
            a. Update item['cost']  = (LARGE_ENVELOPE_ADD_OZ * (i - 1))
            c. Add a break so the loop doesn't continue once the condition is met
3) Finally, print the cost using print_cost().
    a) For standard and irregular envelopes:
        1. Print the cost of mailing the item.
        2. Print how many forever stamps and additional ounce stamps they'll need.
        3. Print the current value of forever stamps and additional ounce stamps.
        4. Link to USPS website to let user purchase stamps.
    b) For large envelopes:
        1. Print the cost of mailing the item.
        2. Print the current denominations of definitive-value stamps available for purchase.
        3. Link to USPS website to let user purchase stamps.
4) Once this function is finished executing, the program has finished checking the cost of the item in question.
    The program will go back to main() to ask the user if they want to check the cost of another item.
"""


from constants import *

"""
# this function will help determine whether to calculate cost for STANDARD/IRREGULAR envelopes or LARGE envelopes
# it will then execute the appropriate function depending on the item['type'].
# standard/irregular envelopes calculate cost based on standard pricing.
# large envelopes calculate cost based on large pricing.
"""
def calculate_cost(item):

    # calculate standard postage if the item type is a standard or irregular envelope.
    if item['type'] == "standard" or item['type'] == "irregular":
        calculate_standard_postage(item)
    # otherwise, calculate large postage if the item type is a large envelope.
    if item['type'] == "large":
        calculate_large_postage(item)


#################################### HELPER FUNCTIONS ####################################


# calculates cost of postage using standard pricing
def calculate_standard_postage(item):
    # assign variable "base_postage" value saved in FOREVER constant
    base_postage = FOREVER
    item['cost'] = base_postage
    item['add_oz'] = 0

    # calculate price for items more than 1 oz. but less than or equal to 3.5 oz.
    if 1 < item['weight'] <= 3.5:
        for i in range(2,5):
            if item['weight'] <= i:
                # update item['cost']
                item['cost'] = base_postage + (ADDITIONAL_OZ * (i - 1))
                # add extra add_oz
                item['add_oz'] = i - 1
                break
    # all irregular items have an extra 15¢ "add_oz" surcharge. Add 15¢ to the postage cost, and increase add_oz by 1.
    if item['type'] == "irregular":
        item['cost'] += ADDITIONAL_OZ
        item['add_oz'] += 1


# calculates cost of postage using large pricing
def calculate_large_postage(item):
    weight = item['weight']
    base_postage = LARGE_ENVELOPE_BASE
    item['cost'] = base_postage

    if 1 < weight <= 13:
        for i in range(2, 14):
            if weight <= i:
                item['cost'] = base_postage + (LARGE_ENVELOPE_ADD_OZ * (i - 1))
                break
    elif weight > 13:
        print("")
        print('Sorry, your package is too large to be mailed as a letter. 😭')
        print('Please take it to your local USPS store and have it delivered as a parcel. 📦')
        item['type'] = "parcel"


# this function prints the final cost of the postage depending on item['type']
def print_cost(item):
    if item['type'] == "standard" or item['type'] == "irregular":
        print_standard_pricing(item)
    elif item['type'] == "large":
        print_large_pricing(item)


# prints pricing to mail standard/irregular item out.
# prints number of FOREVER and ADDITIONAL_OUNCE stamps to use.
# prints current value of FOREVER and ADDITIONAL_OUNCE stamps.
# prints link to buy stamps.
def print_standard_pricing(item):
    print("")
    print("The cost of mailing your item is $%.2f. 💸" % item['cost'])
    if item['add_oz'] == 0:
        print("You can use 1 FOREVER STAMP to mail this item.")
        print("Forever stamps are currently worth $", str(FOREVER) + ".")
    # because I care about singular versus plural harharhar
    elif item['add_oz'] == 1:
        print("You can use 1 FOREVER STAMP and 1 ADDITIONAL OUNCE STAMP to mail this item.")
        print("Forever stamps are currently worth $", str(FOREVER),
              "and Additional Ounce stamps are currently worth $", str(ADDITIONAL_OZ) + ".")
    else:
        print("You can use 1 FOREVER STAMP and " + str(item['add_oz']) +
              " ADDITIONAL OUNCE STAMPS to mail this item.")
        print("Forever stamps are currently worth $", str(FOREVER),
              "and Additional Ounce stamps are currently worth $", str(ADDITIONAL_OZ) + ".")
    exitable_input("Don't have stamps? Support USPS by buying stamps here: "
          "https://store.usps.com/store/results/stamps/_/N-9y93lv (Hit enter to continue)")


# prints pricing to mail large item/small item above 3.5 oz. out.
# only prints the cost of mailing the item
    # FOREVER/ADDITIONAL_OUNCE stamps don't work on larger envelopes (you have to use monetary value stamps.)
# prints values of definitive value stamps user can buy.
#
def print_large_pricing(item):
    print("")
    print("The cost of mailing your item is $%.2f. 💸" % item['cost'])
    print("This is because pricing for mailing out large envelopes starts at $" + str(LARGE_ENVELOPE_BASE),
          "and every additional ounce costs an additional $%.2f" % LARGE_ENVELOPE_ADD_OZ + ".")
    print("You can purchase definitive-value stamps in values of", DEFINITIVE_PRICING_DENOMINATIONS + ".")
    exitable_input("Don't have stamps? Support USPS by buying stamps here: "
          "https://store.usps.com/store/results/stamps/_/N-9y93lv (Hit enter to continue)")

"""
### check_item() ###
This function will check the type of the item.
1) First, it needs to check if the item is a postcard.
    a) if it IS a postcard, program should print the cost/num of stamps to use. Set item type to 'postcard'.
    b) then, exit out of this function to return to main() -> will ask user if they want to check another item
2) If it is NOT a postcard, program should move onto checking if it's a standard envelope.
    a) if it IS a standard envelope, program should execute check_envelope_type() to check if it's
        a standard envelope or irregular envelope. check_envelope_type() will set item type.
    b) then, exit out of this function to return to main() -> continue to take weight of item.
3) Finally, if it is NEITHER a postcard, standard, or irregular envelope, program should check if it's a large envelope
    a) if it's a large envelope, it should set item's type to 'large'.
        Then, exit out of this function to return to main() -> continue to take weight of item.
    b) If it is none of the above, this means it's too large to be an envelope, and needs to be mailed as a parcel.
        Set item's type to 'parcel'.
    c) then, exit out of this function to return to main() -> will ask user if they want to check another item.
"""

from constants import POSTCARD, exitable_input


# main function to check size
def check_item(item):
    # special case for postcard - if it's a postcard, it can simply print the result and exit the function
    check_postcard(item)

    # if the item isn't a postcard, move on and check if it's a standard, irregular, or large envelope
    if not item['type'] == "postcard":
        check_standard_envelope(item)
        # runs if it's not postcard, standard, or irregular -> checks if it's a large or parcel
        if not item['type'] == "standard" and not item['type'] == "irregular":
            check_large_envelope(item)


#################################### HELPER FUNCTIONS ####################################


# check if item is a postcard
def check_postcard(item):
    # create key 'type' for item and set it to an empty string
    item['type'] = ""
    print("")
    print('Is your item a POSTCARD? 🗺')
    print('(Postcards cannot be more than 6" in length and 4.25" in width.)')
    size = exitable_input('Please enter "yes" or "no": ')

    # this runs if the item is a postcard. Print the cost, what kinds of stamps to use, and where to purchase stamps
    if size.lower() == "yes":
        # update item type to postcard
        item['type'] = "postcard"
        print("")
        print("The cost of mailing a postcard is $" + str(POSTCARD) + ".")
        print("You can use 1 POSTCARD STAMP to mail this item.")
        exitable_input("Don't have stamps? Support USPS by buying stamps here: "
                       "https://store.usps.com/store/results/stamps/postcard/_/N-9y93lvZ17vjvm6 (Hit enter to continue)")
    # catches input errors
    elif not size.lower() == "yes" and not size.lower() == "no":
        print("")
        print("Sorry, that's not a valid answer. Try again.")
        return check_postcard(item)


# check for regular sized envelopes
def check_standard_envelope(item):
    print("")
    print('Is your envelope the same size/smaller than a regular, standard-sized envelope? 📨️')
    print('(A regular, standard-sized envelope is defined as 11.5" x 6.125".)')
    size = exitable_input('Please enter "yes" or "no": ')

    # this runs if it's a regular sized envelope
    if size.lower() == "yes":
        # will set item type to "rectangle" or "irregular"
        get_envelope_type(item)
    # catches input errors
    elif not size.lower() == "yes" and not size.lower() == "no":
        print("")
        print("Sorry, that's not a valid answer. Try again.")
        return check_standard_envelope(item)


# check for large sized envelopes
def check_large_envelope(item):
    print("")
    print('Is your envelope smaller than a LARGE-SIZED envelope? 🗂')
    print('(A large-sized envelope is defined as 15" x 11.5".)')
    size = exitable_input('Please enter "yes" or "no": ')

    # this runs if it's small enough to be delivered as a large-envelope letter.
    if size.lower() == "yes":
        # set item type to 'large'
        item['type'] = "large"
        print("")
        print('Great! It looks like you can mail your letter as a LARGE SIZED ENVELOPE. 😀️')
    # this runs if it's too large to be delivered as a letter, and must be delivered as parcel.
    elif size.lower() == "no":
        # set item type to 'parcel'
        item['type'] = "parcel"
        print("")
        print('Sorry, your package is too large to be mailed as a letter. 😭')
        print('Please take it to your local USPS store and have it delivered as a parcel. 📦')
    # catches input errors
    elif not size.lower() == "yes" and not size.lower() == "no":
        print("")
        print("Sorry, that's not a valid answer. Try again.")
        return check_large_envelope(item)


# for regular sized envelopes, set the type of envelope (standard or irregular): they have different pricing
def get_envelope_type(item):
    print("")
    print("Is your envelope a STANDARD rectangle shape, or an IRREGULAR shape (for example, a square)?")
    envelope_type = exitable_input('Please enter "standard" or "irregular": ')

    if envelope_type.lower() == 'standard':
        # check if the regular rectangle envelope contains items. Regular envelopes containing items have a surcharge.
        items = has_items()
        # this code runs if the envelope contains items. We set the item type to 'irregular'.
        if items:
            item['type'] = 'irregular'
            print("")
            print("Alright! You can mail your letter as an IRREGULAR item. 😀")
        # otherwise, this code runs if there are no items and sets the item type as 'standard'.
        elif not items:
            item['type'] = 'standard'
            print("")
            print("Good news! You can mail your letter as a STANDARD item. 😀")
    elif envelope_type.lower() == 'irregular':
        # this sets item type as 'irregular'.
        item['type'] = 'irregular'
        print("")
        print("Good news! You can mail your letter as a IRREGULAR item. 😀")
    # catches input errors
    elif not envelope_type.lower() == "standard" and not envelope_type.lower() == "irregular":
        print("")
        print("Sorry, that's not a valid answer. Try again.")
        return get_envelope_type(item)


# HELPER FUNCTION to check_size(). Will return if a regular envelope contains items (making it irregular) or not.
def has_items():
    print("")
    print("Does your item contain items such as pens, pencils, or keys that make it IRREGULARLY SHAPED? 🖋")
    answer = exitable_input('Please enter "yes" or "no": ')
    if answer.lower() == "yes":
        return True
    elif answer.lower() == "no":
        return False
    elif not answer.lower() == "yes" and not answer.lower() == "no":
        print("")
        # catches input errors
        input("Sorry, that's not a valid answer. Try again. (Hit enter)")
        return has_items()

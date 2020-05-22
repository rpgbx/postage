"""
These are the current prices of stamps.
* Forever Stamps are currently worth 55¢.
* Additional Oz. Stamps are currently worth 15¢.
* Postcard Stamps are currently worth 35¢.
* Large Envelopes start at $1.00.
* Each additional ounce for large envelopes is 20¢.
* You can currently purchase definitive stamps in denominations of $1, $2, $5, and $10.

Last Updated: May 19, 2020
"""

import sys

FOREVER = 0.55
ADDITIONAL_OZ = 0.15
POSTCARD = 0.35
LARGE_ENVELOPE_BASE = 1
LARGE_ENVELOPE_ADD_OZ = 0.20
DEFINITIVE_PRICING_DENOMINATIONS = "$1, $2, $5, and $10"


# this helper function checks if the user has typed "exit" to kill the program at any time.
def exitable_input(input_text):
    user_response = input(input_text)
    if user_response.lower() == "exit":
        print("")
        print("Thanks for using Postage Calculator! 🥳")
        sys.exit(0)
    else:
        return user_response

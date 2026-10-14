## WHAT IS STRINGS METHODS?
"""
 Strings methods are built-in functions that can be called on string objects to perform various operations on them.
"""

## COMMON STRING METHODS

# ~1. Classification Methods
"""
 These methods are used to classify or check the nature of the string.
 Returns True or False based on the condition.

  * .isalpha() --> Checks if all characters in the string are alphabetic.
  * .isdigit() --> Checks if all characters in the string are digits.
  * .isalnum() --> Checks if all characters in the string are alphanumeric (letters and numbers).
  * .isspace() --> Checks if all characters in the string are whitespace.
"""
phone_input = "12345"
print(phone_input.isdigit())  # Output: True


# ~2. Search & Location Methods
"""
 These methods are used to search for a substring within a string and return its position or check its existence.

  * .find(substring) --> Returns the lowest index of the substring if found, otherwise returns -1.
  * .index(substring) --> Similar to find(), but raises a ValueError if the substring is not found.
  * .count(substring) --> Returns the number of occurrences of the substring in the string.
  * .startswith(prefix) --> Checks if the string starts with the specified prefix.
  * .endswith(suffix) --> Checks if the string ends with the specified suffix.
"""
email = "developer@domain.com"

# Find the position of the "@" symbol
print(email.find("@"))       # Output: 9

# Verify the domain extension
print(email.endswith(".com")) # Output: True


# ~3. Transformation Methods
"""
 These methods are used to change the case or format of the string.

  * .upper() --> Converts all characters in the string to uppercase.
  * .lower() --> Converts all characters in the string to lowercase.
  * .capitalize() --> Capitalizes the first character of the string and lowercases the rest.
  * .title() --> Capitalizes the first character of each word in the string.
  * .swapcase() --> Swaps the case of each character in the string.
""" 
raw_data = "  URGENT: Action Required  "

cleaned = raw_data.strip().lower()
print(cleaned) 
# Output: "urgent: action required"


# ~4. Advanced Manipulation
"""
 These methods are used for more complex string manipulations.

  * .replace(old, new) --> Replaces all occurrences of the old substring with the new substring.
  * .split(separator) --> Splits the string into a list of substrings based on the specified separator.
  * .join(iterable) --> Joins elements of an iterable (like a list) into a single string, separated by the string on which it is called.
"""
# Splitting text into a list
csv_line = "Tesla,SpaceX,Neuralink"
companies = csv_line.split(",")
print(companies)  
# Output: ['Tesla', 'SpaceX', 'Neuralink']

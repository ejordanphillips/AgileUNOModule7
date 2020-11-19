"""
Jordan Phillips
Module 7 Assignment
"""


# 1. Import my_module and prettyprint

import my_module 

import pprint

# 2. Use the greeting method from my_module to print your name

my_module.greeting("Jordan")

# 3. Use letter_text function to print a string

kwargs = {
    'name': 'Jordan',
    'amount': '500',
    'denomination': 'dollars',
    }

my_module.letter_text(**kwargs)

# 4. Import  my_json_data and print

from my_module import my_json_data
print(my_json_data)

# 5. Import my_json_data as my_data and print using prettyprint

from my_module import my_json_data as my_data
pp = pprint.PrettyPrinter(indent=3)
pp.pprint(my_data)





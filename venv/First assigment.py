"""
Assignment 1: Andrea Perez Lopez, Simone Nørgaard

Exercise 1.
"""
hundred_digit_str = "731671765313306249192251" \
                    "196744265747423553491949349" \
                    "6983520312774506326239578318" \
                    "016984801869478851843"


# Defining the function


def consecutive_func(inputstring):
    consecutive = 4
    inputstring = [int(ch) for ch in inputstring]
    max_result = 0
    for i in range(len(inputstring) - consecutive + 1):
        result = inputstring[i] * inputstring[i + 1] * inputstring[i + 2] * inputstring[
            i + 3]
        if result > max_result:
            max_result = result

    return print(max_result)

# Using the function in the list


consecutive_func(hundred_digit_str)


""" 
 Exercise 2 
"""


def splitoddoeven(tlist):
    list_even = []
    list_odd = []

    for i in tlist:
        if i % 2 == 0:
            list_even.append(i)
        else:
            list_odd.append(i)

    return print("The list have these even numbers:", list_even, "and these odd:", list_odd)


list_01 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
splitoddoeven(list_01)

""" 
Exercise 3 Simone is going to introduce the answer

"""

""" 
Exercise 4 Simone is going to introduce the e answer 

"""

str = "ccgatcahctatttaaaaccctatcatastadfa".lower()
word = "cat"
coun_ans = len(str)
for i in word:
    coun_ans = min(coun_ans, str.count(i)//word.count(i))
print(coun_ans)

""" 
Exercise 5 

"""

def breakfunc(test_string):
    new_string = ""
# Replacing non-alphanumeric numbers with spaces
    for ch in test_string:
        if ch == " ":
            new_string += ch
        if ch.isalnum():
            new_string += ch
        if not ch.isalnum():
            new_string += " "

# Analyze each word
# mod_string is formed by replacing numeric words with an _
# num_string is formed by omitting each item which is not a number
    new_string = new_string.split()
    mod_string = ["_" if item.isnumeric() else item for item in new_string]
    num_string = [item for item in new_string if item.isnumeric()]
# joining is used for creating the lists.
    mod_string = "".join(mod_string)
    num_string = "_".join(num_string)
    res = (mod_string, num_string)
    print(res)

# Testing the function


string_to_parse = 'Copenhagen hosted Cop-09 summit' \
                    ' at Bella Center in 2009, which' \
                    ' was attended by delegates from' \
                    ' more than 100 countries.'

breakfunc(string_to_parse)

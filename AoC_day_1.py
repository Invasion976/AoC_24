import requests
from AoC_API import get_input
import logging
logging.basicConfig(level=None)


result = get_input(1)
left_data = []
righ_data = []


for row in result:
    
    row_list = row.split()

    left_data += [ int(row_list[0].strip()) ]
    righ_data += [ int(row_list[1].strip()) ]


def list_recursion(list_one, list_two):
    """
    uses recursion to get the total difference between the two lists of numbers

    Arguments:
        list_one -------- (list of int) list of numbers one
        list_two -------- (list of int) list of numbers two

    Returns:
        ----------------- (int) total difference
    """

    if len(list_one) == 0:
        return 0
    
    min_one = list_one.pop(list_one.index(min(list_one)))
    min_two = list_two.pop(list_two.index(min(list_two)))

    return list_recursion(list_one, list_two) + (int(max(min_one, min_two)) - int(min(min_one, min_two)))


def get_diff():
    """
    Gets the difference between two lists.

    Returns:
        total_diff -------- (int) total difference between the two lists
    """

    total_diff = list_recursion(left_data, righ_data)

    return(total_diff)


def similarity_score(list_one, list_two):
    """
    Determines similarity by multiplying each number in the first list by the frequency
        in which it appears in the second list. Then returns the total.

    Arguments:
        list_one -------- (list of int) first list of numbers
        list_two -------- (list of int) second list of numbers

    Returns:
        total ----------- (int) sum of similarity scores
    """
    totals = []

    for num_one in list_one:
        multiplier = 0

        for num_two in list_two:
            if num_one == num_two:
                multiplier += 1
        
        totals += [ num_one * multiplier ]

    return sum(totals)


def sim_score():
    """
    """

    return similarity_score(left_data, righ_data)
        
from AoC_API import get_input

temp_data_list = get_input(2)
data_list = []

for num_string in temp_data_list:
    num_list = num_string.strip().split()
    temp_list = []
    for num in num_list:
        temp_list += [ int(num) ]
    data_list += [ temp_list ]


def isIncreasing(number_list, direction='none'):
    """
    Checks if list of number is all increasing or decreasing

    Arguments:
        number_list ------- (list of int) list of numbers

    Returns:
        ------------------- (bool) if all increasing or decreasing
    """

    if len(number_list) == 1:
        return True
    
    else:
        if number_list[0] < number_list[1]:
            if direction == 'none':
                direction = 'increasing'
            elif direction == 'decreasing':
                return False
        
        elif number_list[0] > number_list[1]:
            if direction == 'none':
                direction = 'decreasing'
            elif direction == 'increasing':
                return False
            
        return isIncreasing(number_list[1:], direction)


def isSafe(number_list):
    """
    Determines if the list of numbers is 'safe'

    Arguments:
        number_list -------- (list of int) list of numbers

    Returns:
        -------------------- (bool) if number is safe
    """

    if not isIncreasing(number_list):
        return False

    for i in range(len(number_list) - 1):
        n_max = max(number_list[i], number_list[i + 1])
        n_min = min(number_list[i], number_list[i + 1])

        if n_max - n_min > 3 or n_max - n_min == 0:
            return False
        
    return True


def safeCount(number_lists):
    """
    Counts the number of safe lists of numbers

    Arguments:
        number_list -------- (list of int) number list

    Returns:
        -------------------- (int) number of safe lists
    """

    count = 0

    for num_list in number_lists:
        if isSafe(num_list):
            count += 1
    
    return count


def safeIfRemoved(number_list):
    """
    Checks if list with element removed is safe.

    Arguments:
        number_list -------- (list of int) list of numbers

    Returns:
        -------------------- (bool) if list is now safe
    """

    for number in number_list:
        new_list = number_list
        print(new_list)
        new_list.remove(number)
        print(new_list)
        new_list = number_list
        if isSafe(new_list):
            return True
    return False


def ifRemovedCount(number_lists):
    """
    Counts number of lists made safe by removal of a single item.

    Arguments:
        number_list -------- (list of int) list of numbers

    Returns:
        -------------------- (int) count of safe lists
    """

    count = 0

    for num_list in number_lists:
        if safeIfRemoved(num_list) and not isSafe(num_list):
            count += 1

    return count


def getAnswer1():
    """
    Gets the first AoC answer

    # The levels are either all increasing or all decreasing.
    # Any two adjacent levels differ by at least one and at most three.

    Returns:
        ------------ (int) count of safe number lists
    """

    return safeCount(data_list)


def getAnswer2():
    """
    Gets the second AoC answer

    # Now, the same rules apply as before, 
    # except if removing a single level from an unsafe report would make it safe, 
    # the report instead counts as safe.

    Returns:
        ------------ (int) count of number lists that were made safe
    """
    previous = getAnswer1()
    total = previous + ifRemovedCount(data_list)
    return total
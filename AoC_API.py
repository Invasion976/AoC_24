import requests
import sys
import os

sessionToken = os.getenv('AOC_TOKEN')


def request_data(day):
    """
    Requests input data from AoC website for the given day.

    Arguments:
        day -------- (int) day to check for data
    """

    target_url = 'https://adventofcode.com/2024/day/' + str(day) + '/input'
    AoC_header = { 'Cookie':sessionToken }
    request = requests.get(target_url, headers=AoC_header)

    if request.status_code == 200:
        return request.text
    
    else:
        sys.exit(f"/api/alerts response: {request.status_code}: {request.reason} \n{request.content}")


def get_input(day):
    """
    Gets the Advent of Code input for the given day.

    Arguments:
        day -------- (int) day to check for data
    """

    data_list = []
    look_string = 'Day ' + str(day)

    try:

        input_data_file = open("AoC_input_data.txt", "r")
        percept = False

        for line in input_data_file.readlines():
            if percept == True:
                data_list += [ line ]

            else:
                if look_string in line:
                    percept = True

                elif 'Day ' in line and look_string not in line:
                    percept = False

        if len(data_list) == 0:
            
            data_list = request_data(day)

    except:

        input_data_file = open("AoC_input_data.txt", "x")





    input_data_file.close()


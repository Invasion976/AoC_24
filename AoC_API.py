import requests
import sys
import os
import logging

logging.basicConfig(
    level=None,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('debug.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

sessionToken = os.getenv('AOC_TOKEN')
logger.debug(f"Session token present: {bool(sessionToken)}")  # Check if we have a token

def request_data(day):
    """
    Requests input data from AoC website for the given day.

    Arguments:
        day -------- (int) day to check for data
    """

    logger.debug(f'Entering request_data for day {day}')

    target_url = 'https://adventofcode.com/2024/day/' + str(day) + '/input'
    AoC_header = { 'Cookie':sessionToken }

    try:
        request = requests.get(target_url, headers=AoC_header)
        logger.debug(f'Request status code: {request.status_code}')

        if request.status_code == 200:
            logger.debug(f'Request successful, text length: {len(request.text)}')
            return request.text
        
        else:
            error_msg = f"API request failed: {request.status_code}: {request.reason}\n{request.content}"
            logger.error(error_msg)
            raise requests.RequestException(error_msg)
        
    except Exception as e:
        logger.exception("Exception in request_data:")
        raise  # Re-raise the exception after logging it       


def get_input(day):
    """
    Gets the Advent of Code input for the given day.

    Arguments:
        day -------- (int) day to check for data
    """
    logger.debug(f'Entering get_input for day {day}')
    data_list = []
    look_string = 'Day ' + str(day)

    try:
        logger.debug('Attempting to open input file')
        with open("AoC_input_data.txt", "r") as input_data_file:
            percept = False
            for line in input_data_file.readlines():
                logger.debug(f'Processing line: {line.strip()}')                
                if percept == True:
                    data_list += [ line ]

                else:
                    if look_string in line:
                        percept = True
                        logger.debug('Found matching day')
                    elif 'Day ' in line and look_string not in line or line == '':
                        percept = False

        logger.debug(f'File processing complete. Data list length: {len(data_list)}')

        if len(data_list) == 0:
            logger.debug('No data found in file, requesting from API')
            data_list = request_data(day)
            logger.debug('Writing new data to file')
            with open("AoC_input_data.txt", "a") as input_data_file: # did not have previously
                input_data_file.write(f'\n{look_string}\n')
                input_data_file.write(data_list)

    except FileNotFoundError:
        logger.debug('Input file not found, creating new file')
        data_list = request_data(day)
        with open("AoC_input_data.txt", "w") as input_data_file:
            input_data_file.write(f'{look_string}\n')
            input_data_file.write(data_list)

    except Exception as e:
        logger.exception("Unexpected error in get_input:")
        raise

    logger.debug(f'Returning data list of length: {len(data_list)}')
    return data_list


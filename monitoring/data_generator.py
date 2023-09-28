import json
from random import randint
from typing import Final
import schedule
import time


DATA_PATH: Final = './data/data.json'


def write_to_json_file():
    test_data = {
        'age': randint(18, 100),
        'm': randint(18, 100),
        'P': randint(18, 100)
    }
    with open(DATA_PATH, 'w') as json_file:
        json.dump(test_data, json_file)


if __name__ == '__main__':
    write_to_json_file()
    schedule.every(1).minutes.do(write_to_json_file)
    while True:
        print('Process...')
        schedule.run_pending()
        time.sleep(10)

# write a code to log the following:
# 1. the current date and time
# 2. the name of the user
# 3. the name of the machine
# 4. the name of the current directory
# 5. the name of the current file


import os
import time as t
from termcolor import colored

def log_info(msg: str) -> None:
    """
    This function will log the following:
    1. the current date and time
    2. the name of the user
    3. the name of the machine
    4. the name of the current directory
    5. the name of the current file
    """
    date = t.strftime("%d/%m/%Y")
    # time in 12 hour format
    time = t.strftime("%I:%M:%S %p")
    user = os.getlogin()
    host = os.uname()[1]
    dir = os.getcwd()
    file = os.path.basename(__file__)
    # print each of the above variables on a new line in the following format:
    # Date: DD/MM/YYYY
    # Time: HH:MM:SS (12 hour format)
    # User: user_name
    # Host: host_name
    # Dir: current_dir
    # File: current_file
    print(colored("Message: {}\nDate: {}\nTime: {}\nUser: {}\nHost: {}\nDir: {}\nFile: {}".format(msg, date, time, user, host, dir, file), "red"))


if __name__ == "__main__":
    log_info('Hi!')
    # help(log_info)

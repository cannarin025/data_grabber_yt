from decimal import Decimal
from datetime import datetime

#works out number of seconds elapsed since a time of 00:00:00
def seconds_elapsed(time_string):
    zero_time = datetime.strptime("00:00:00", "%H:%M:%S")
    if len(time_string.split(":")) == 3:
        time = datetime.strptime(time_string, "%H:%M:%S")
    elif len(time_string.split(":")) == 2:
        time = datetime.strptime(time_string, "%M:%S")
    elif len(time_string.split(":")) == 1:
        return int(time_string)
    else:
        raise Exception("Error! Inputted time could not be understood.")

    seconds = (time - zero_time).total_seconds()
    return seconds

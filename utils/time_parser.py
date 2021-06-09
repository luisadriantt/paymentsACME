from datetime import timedelta
""""
    Utils to format and parse hours
"""""


# Returns one day if the hour given is 0
def to_24_hours(hour):
    if hour == timedelta(hours=0):
        return timedelta(hours=24)
    return hour


# Casts the hour to number
def hour_to_number(hour):
    return int(str(hour).split(",")[-1].split(":")[0])


# Casts the given number to hour
def number_to_hour(number):
    return timedelta(hours=number)


# Returns only the hour of a timedelta
def format_hour(hour):
    int_hour = hour_to_number(hour)
    return timedelta(hours=int_hour)


# Returns tuple of numbers from hours
def hours_to_tuple(hour1, hour2):
    int_hour1 = hour_to_number(hour1)
    int_hour2 = hour_to_number(hour2)
    hours_tuple = (int_hour1, int_hour2)
    return hours_tuple

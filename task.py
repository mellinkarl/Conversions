def conv_num(num_str):
    """Converts a number string into a base 10 number"""
    # check if input is a string
    if not isinstance(num_str, str):
        return None
    num_str = num_str.lower()
    # check for negative sign
    if num_str.startswith('-'):
        sign = -1
        num_str = num_str[1:]
    else:
        sign = 1
    # handle hexadecimal numbers
    if num_str.startswith('0x'):
        hex_part = num_str[2:]
        if len(hex_part) > 0 and all(char in '0123456789abcdef' for char in hex_part):
            return sign * int(num_str, 16)
        else:
            return None


def my_datetime(num_sec):
    '''Takes a number of seconds since the epoch (1970)
      and returns the date in the format MM-DD-YYYY.'''
    seconds_in_day = 86400
    seconds_in_year = 31536000
    seconds_in_leap_year = 31622400

    # Current year to update
    current_year = 1970

    def is_leap_year(year):
        '''Returns True if the year is a leap year, False otherwise.'''
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return True
        else:
            return False

    # Calculate year
    while num_sec >= seconds_in_year:
        if is_leap_year(current_year):
            num_secs_in_year = seconds_in_leap_year
        else:
            num_secs_in_year = seconds_in_year
        if num_sec >= num_secs_in_year:
            num_sec -= num_secs_in_year
            current_year += 1

    if is_leap_year(current_year):
        february = 29
    else:
        february = 28
    # Determing the number of days in each month (leap year or not)
    days_in_months = [31, february, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Calculate month
    current_month = 1
    for numDays in days_in_months:
        # More than the seconds in current month remaining
        if num_sec >= seconds_in_day * numDays:
            num_sec -= seconds_in_day * numDays
            current_month += 1
        # Less than the seconds in current month remaining
        else:
            break

    # Calculate day (add one for the current day)
    current_day = num_sec // seconds_in_day + 1

    return f'{current_month:02d}-{current_day:02d}-{current_year}'

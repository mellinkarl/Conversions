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
        if len(hex_part) < 1 or not all(char in '0123456789abcdef' for char in hex_part):
            return None
        return sign * hex_str_to_int(hex_part)

    # handle floating-point numbers
    if '.' in num_str:
        if num_str.count('.') > 1:
            return None
        try:
            return sign * str_to_float(num_str)
        except ValueError:
            return None

    # handle integer numbers
    try:
        return sign * str_to_int(num_str)
    except ValueError:
        return None


def str_to_int(num_str):
    """Helper function to convert an integer string to an int"""
    if not num_str.isdigit():
        raise ValueError
    result = 0
    digits = "0123456789"
    # calculate each digit
    for digit in num_str:
        result = result * 10 + digits.index(digit)
    return result


def str_to_float(num_str):
    """Helper function to convert a string with one decimal point to a float"""
    integer_part, decimal_part = num_str.split('.')
    # check if string is "."
    if len(integer_part) == 0 and len(decimal_part) == 0:
        raise ValueError
    # handle numbers with decimal point at the start or end
    if len(integer_part) == 0:
        integer_part = "0"
    if len(decimal_part) == 0:
        decimal_part = "0"
    # check if all characters are digits
    if not integer_part.isdigit() or not decimal_part.isdigit():
        raise ValueError
    result = str_to_int(integer_part)
    factor = 0.1
    # calculate decimal places
    for digit in decimal_part:
        result += str_to_int(digit) * factor
        factor /= 10
    return round(result, len(decimal_part))


def hex_str_to_int(num_str):
    result = 0
    hex_digits = '0123456789abcdef'
    # calculate each base-16 digit
    for digit in num_str:
        result = result * 16 + hex_digits.index(digit)
    return result


def my_datetime(num_sec):
    """Takes a number of seconds since the epoch (1970) and returns the date in the format MM-DD-YYYY."""
    seconds_in_day = 86400
    seconds_in_year = 31536000
    seconds_in_leap_year = 31622400

    # Current year to update 
    current_year = 1970

    def is_leap_year(year):
        """Returns True if the year is a leap year, False otherwise."""
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return True
        else:
            return False
        
    # Calculate year
    while num_sec >= seconds_in_year:
        num_secs_in_year = seconds_in_leap_year if is_leap_year(current_year) else seconds_in_year
        if num_sec >= num_secs_in_year:
            num_sec -= num_secs_in_year
            current_year += 1

    # Determing the number of days in each month (leap year or not)
    days_in_months = [31, 29 if is_leap_year(current_year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

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


print(my_datetime(0))
print(my_datetime(123456789))
print(my_datetime(9876543210))
print(my_datetime(201653971200))


def conv_endian(num, endian='big'):
    pass

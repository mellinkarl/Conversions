def conv_num(num_str):
    """Converts a number string into a base 10 number"""
    # check if input is a string
    if not isinstance(num_str, str):
        return None
    num_str = num_str.lower()

    # handle hexadecimal numbers
    if num_str.startswith('0x') or num_str.startswith('-0x'):
        return hex_str_to_int(num_str)

    # handle floating-point numbers
    if '.' in num_str:
        return str_to_float(num_str)

    # handle integer numbers
    return str_to_int(num_str)


def str_to_int(num_str):
    """Helper function to convert an integer string to an int"""
    sign = -1 if num_str.startswith('-') else 1
    num_str = num_str[1:] if num_str.startswith('-') else num_str

    # check if the string is not all digits
    if not num_str.isdigit():
        return None
    result = 0
    digits = "0123456789"
    # calculate each digit
    for digit in num_str:
        result = result * 10 + digits.index(digit)
    return sign * result


def str_to_float(num_str):
    """Helper function to convert a floating-point number string to a float"""
    sign = -1 if num_str.startswith('-') else 1
    num_str = num_str[1:] if num_str.startswith('-') else num_str
    if num_str.count('.') > 1:
        return None

    # split string into integer and decimal strings
    integer_part, decimal_part = num_str.split('.')
    if len(integer_part) == 0 and len(decimal_part) == 0:
        return None
    # handle numbers with decimal point at the start or end
    if len(integer_part) == 0:
        integer_part = "0"
    if len(decimal_part) == 0:
        decimal_part = "0"
    # check if all characters are digits
    if not integer_part.isdigit() or not decimal_part.isdigit():
        return None
    result = str_to_int(integer_part)
    factor = 0.1
    # calculate decimal places
    for digit in decimal_part:
        result += str_to_int(digit) * factor
        factor /= 10
    return sign * round(result, len(decimal_part))


def hex_str_to_int(num_str):
    sign = -1 if num_str.startswith('-') else 1
    num_str = num_str[1:] if num_str.startswith('-') else num_str

    hex_part = num_str[2:]
    hex_digits = '0123456789abcdef'
    # check if the hex number is empty or containing non-hex characters
    if len(hex_part) < 1 or not all(char in hex_digits for char in hex_part):
        return None
    result = 0
    # calculate each base-16 digit
    for digit in hex_part:
        result = result * 16 + hex_digits.index(digit)
    return sign * result


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
    # Determine the number of days in each month (leap year or not)
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


def conv_endian(num, endian='big'):
    neg_flag = num < 0
    pos_num = abs(num)

    def int_to_hex(digit):
        hex_chars = "0123456789ABCDEF"
        hexer = ""
        if digit == 0:
            return "0"
        while digit > 0:
            remainder = digit % 16
            hexer = hex_chars[remainder] + hexer
            digit = digit // 16
        return hexer

    hex_str = int_to_hex(pos_num)

    hex_length = len(hex_str)
    if hex_length % 2 != 0:
        hex_str = "0" + hex_str

    byte_list = []
    hex_length = len(hex_str)
    for i in range(0, hex_length, 2):
        byte = hex_str[i:i+2]
        byte_list.append(byte)

    if endian == 'little':
        byte_list.reverse()
    elif endian == 'big':
        pass
    else:
        return None

    result = byte_list
    result = ' '.join(result)
    if neg_flag:
        result = '-'+result
    return result

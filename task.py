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
    '''Takes a number of seconds since the epoch (1970) and returns the date in the format MM-DD-YYYY.'''
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
    neg_flag = num < 0
    Postive_num = abs(num)
    def int_to_hex(num):
        hex_chars = "0123456789ABCDEF"
        hex_str = ""
        if num == 0:
            return "0"
        while num > 0:
            remainder = num % 16
            hex_str = hex_chars[remainder] + hex_str
            num = num // 16
        return hex_str

    hex_str = int_to_hex(Postive_num)

    hex_length = len(hex_str)
    if hex_length % 2 != 0:
        hex_str = "0" + hex_str

    byte_list = []
    hex_length = len(hex_str)
    for i in range(0,hex_length,2):
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


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
    pass


def conv_endian(num, endian='big'):
    pass

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


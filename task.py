def conv_num(num_str):
    '''Hexadecimal Portion'''
    if num_str.lower().startswith('0x'):
        hex_part = num_str[2:]
        if all(char in '0123456789abcdefABCDEF' for char in hex_part):
            return int(num_str, 16)
        else:
            return None


print(conv_num('0xAD4'))
print(conv_num('0Xad4'))
print(conv_num('0xAZ4'))
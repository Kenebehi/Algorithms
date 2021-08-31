def binary_to_decimal(binary, num=0):
    """
    Convert binary number to decimal
    :param binary:
    :param num:
    :return: int
    """
    binary = str(binary)

    if not binary:
        return num

    num += int(binary[0]) * 2 ** (len(binary) - 1)
    return binary_to_decimal(binary[1:], num)


bin_num = 101100101
bin_num2 = 101011110110010
bin_num3 = 10001001001011100100
print(binary_to_decimal(bin_num3))

def decimal_to_binary(dec, binary_number=''):
    """
    Convert decimal to binary number
    :param dec:
    :param binary_number:
    :return:
    """
    if dec < 2:
        return (binary_number + '1')[::-1]

    if dec >= 2:
        binary_number = binary_number + str(dec % 2)
        return decimal_to_binary(dec//2, binary_number)


decimal = 357
decimal2 = 18
decimal3 = None
decimal4 = 22450
decimal5 = 561892
print(decimal_to_binary(decimal5))

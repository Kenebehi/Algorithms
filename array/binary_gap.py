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


def _binary_gap(num, count=0, m=0):
    """
    if value is one start counting zeros
    :param num:
    :param count:
    :return:
    """
    if not num:
        return m

    if num[0] == '1':
        print(count, m, num)
        if count > m:
            m, count = count, 0
            return _binary_gap(num[1:], count, m)
        count = 0
        return _binary_gap(num[1:], count, m)
    if num[0] == '0':
        count += 1
        return _binary_gap(num[1:], count, m)
    return m


def binary_gap(num):
    """
    A binary gap within a positive integer N is any maximal sequence of
    consecutive zeros that is surrounded by ones at both ends in the binary
    representation of N.

    For example, number 9 has binary representation 1001 and contains a binary
    gap of length 2. The number 529 has binary representation 1000010001
    and contains two binary gaps: one of length 4 and one of length 3.
    The number 20 has binary representation 10100 and contains one binary
    gap of length 1. The number 15 has binary representation 1111 and has
    no binary gaps. The number 32 has binary representation 100000 and has
    no binary gaps.
    :param num:
    :return:
    """
    num = decimal_to_binary(num)
    print(num)
    return _binary_gap(num)


num = 100
num2 = 1001
num3 = 10001001
num4 = None
num5 = 11000000000000000000000000010
num6 = 100011101101110100011100001
num7 = 111
num8 = 1011_2
num9 = 561892  # 10001001001011100100
num10 = 1041
print(binary_gap(num9))

def _non_increasing_integer(arry):
    """
    private method
    :param arry:
    :return:
    """
    try:
        if arry[0] == arry[1]:
            print(f"The current value is {arry[0]} the next val is {arry[1]}")
            return _non_increasing_integer(arry[1:])
        if arry[0] + 1 == arry[1]:
            return _non_increasing_integer(arry[1:])
        return arry[0] + 1
    except:
        return arry[0] + 1


def non_increasing_integer(arry):
    """
    given an array find the first non increasing non integer
    ex.
    [-1, 0, 1, 2, 3, 5] Ans. 4
    :param arry:
    :return:
    """
    # sort arrray
    arry.sort()

    if len(arry) == 0:
        return f"the array is empty {arry}"
    if arry[-1] <= 0:
        return 1
    return _non_increasing_integer(arry)


arry = [-1, 0, 1, 2, 3, 5]
arry2 = [-3, -4, -2]
arry3 = [1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4, 5]
print(non_increasing_integer(arry3))

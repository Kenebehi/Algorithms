def remove_duplicates(arry, arry2=[]):
    """

    :param arry:
    :return:
    """
    last = arry[-1]

    if arry[0] == last:
        return arry2 + [arry[0]]

    if arry[0] != arry[1]:
        arry2.append(arry[0])
        return remove_duplicates(arry[1:])
    return remove_duplicates(arry[1:])


def remove_duplicates2(arry):
    """
    Kevin Naughton Solution on youtube
    https://www.youtube.com/watch?v=zIHe2V5Py3U
    :param arry:
    :return: length of array
    """
    index = 1
    for i in range(0, len(arry) - 1):
        print(arry[i], arry[i + 1])
        if arry[i] != arry[i + 1]:
            arry[index] = arry[i + 1]
            index += 1
    return index


arry = [1, 2, 3, 3, 4, 4, 5]
arry3 = [1, 2, 3]
arry4 = [1, 1, 1]
arry6 = [1, 2, 3, 6, 6, 6, 6, 6, 6]
print(remove_duplicates2(arry))

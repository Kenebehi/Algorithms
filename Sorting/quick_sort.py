def _quick_sort(arry):
    first = 1
    last = len(arry) - 1
    pivot = 5

    while first <= last:
        if arry[first] <= pivot:
            pass


def quick_sort(arry):
    """
    The quick sort algorithm is very efficient for sorting. The quick sort
     algorithm falls under the divide and conquer class of algorithms,
     similar to the merge sort algorithm, where we break (divide) a problem
      into smaller chunks that are much simpler to solve (conquer).
    :return:
    """
    return _quick_sort(arry)


arry = [5, 6, 2, 3, 6, 9, 10, 22]
quick_sort(arry)
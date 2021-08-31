def two_number_sum(arry, target):
    """
    Given an array find out if two numbers sum up to target

    soln1:
        Use a dict to store numbers as you traverse through the array
    store every number in a hash table, access is constant time. For each
    num in the array check if the number needed to sum up to the target is
    present in the array
    :param arry:
    :param target:
    :return: dict
    """
    nums = {}
    for num in arry:
        potential_match = target - num
        if potential_match in nums:
            return [potential_match, num]
        else:
            nums[num] = True


def two_num_sum(arry, target):
    """
    Given an array find out if two numbers sum up to target

    soln2:
    sort array
    for each traversal throught the array, takr first and last value if they sum
    to target return the values. else  if the current sum is less than
    target then move

    :param arry:
    :param target:
    :return: list
    """
    # sort arrray
    arry.sort()
    # beginning of array
    left = 0
    # end of array
    right = len(arry) - 1

    while left < right:
        current_sum = arry[left] + arry[right]
        if current_sum == target:
            return [arry[left], arry[right]]
        elif current_sum < target:
            left += 1
        elif current_sum > target:
            right -= 1
        return []


arry = [3, 5, -4, 8, 11, 1, -1, 6]
target = 10
print(two_number_sum(arry, target))

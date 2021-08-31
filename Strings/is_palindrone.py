def is_palindrone(word):
    """
    :param word:
    :return: Boolean
    """

    if len(word) <= 1:
        return True

    # aba
    i = 0
    j = len(word) - 1

    while i <= j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True


words = ["", "a", "aba", "abb"]
for word in words:
    print(is_palindrone(word))
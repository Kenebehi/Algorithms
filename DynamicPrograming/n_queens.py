def n_queens(matrix):
    """
    Using backtracking to solve n queens problem as a tree data structure
    - root node is the empty matrix
    - first level tree all positions to place 1st queen
    - second level tree each first level node positions to place second queen
    - n level repeat and rinse
    :param matrix:
    :return:
    """
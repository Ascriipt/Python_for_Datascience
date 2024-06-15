def count_in_list(lits: list, key: str) -> int:
    """
    Args:
        l (list): any list containing n elements
        key (str): a key to match with list values

    Returns:
        int: the number of matching keys
    """
    return (sum(1 for x in lits if x == key))

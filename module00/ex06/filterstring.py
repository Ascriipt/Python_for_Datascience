import sys
import ft_filter


def filterstring(tofilter: str, n: int):
    """_summary_

    Args:
        tofilter (str): the string to parse
        n (int): the length to filter
    """
    parsed_list = [x for x in tofilter.split()]
    print(ft_filter.ft_filter(lambda i: len(i) > n, parsed_list))


def main():
    """_summary_

    Raises:
        AssertionError: in case there aren't enough parameters
    """
    argv = sys.argv
    if len(argv) < 3 or len(argv) > 3:
        raise AssertionError("The arguments are bad")
    else:
        filterstring(argv[1], int(argv[2]))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f'AssertionError: {e}')
    except ValueError as e:
        print(f"ValueError: {e}")

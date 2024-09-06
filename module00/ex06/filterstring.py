import sys
import ft_filter

def filterstring(tofilter: str, n: int):
    """_summary_

    Args:
        tofilter (str): the string to parse
        n (int): the length to filter
    """



def main():
    """_summary_

    Raises:
        AssertionError: in case there aren't enough parameters
    """
    try:
        argv = sys.argv
        if len(argv) < 3 or len(argv) > 3:
            raise AssertionError("The arguments are bad")
        tofilter = argv[1]
        n = int(argv[2])
        parsed_list = [x for x in tofilter.split()]
        print(ft_filter.ft_filter(lambda i: len(i) > n, parsed_list))
    except AssertionError as e:
        print(f'AssertionError: {e}')
    except ValueError as e:
        print(f"ValueError: {e}")


if __name__ == "__main__":
    main()

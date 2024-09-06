def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    Calculate BMI from height and weight data.

    Args:
        height (list[int  |  float]): list of heights
        weight (list[int  |  float]): list of weights

    Returns:
        list[int | float]: list of BMIs
    """
    try:
        if len(height) != len(weight):
            raise RuntimeError("Height and Weight are not the same size.")
        for x, _ in enumerate(height):
            if not isinstance(height[x], (int, float)):
                raise RuntimeError(f"height of {x} is not <'int'> or <'float'>")
            if not isinstance(weight[x], (int, float)):
                raise RuntimeError(f"weight of {x} is not <'int'> or <'float'>")
        return [(weight[i]/(height[i]*height[i])) for i in range(len(height))]
    except RuntimeError as e:
        print(f"RuntimeError: {e}")


def is_limit(x: float | int, limit: int) -> bool:
    """
    returns true if x <= limit
    Args:
        x (float | int): value to compare
        limit (int): value to compare to
    Returns:
        bool
    """
    if int(x) < limit:
        return False
    return True


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    try:
        for x, _ in enumerate(bmi):
            if not isinstance(bmi[x], (int, float)):
                raise RuntimeError(f"bmi of {x} is not <'int'> or <'float'>")
        return [is_limit(i, limit) for i in bmi]
    except RuntimeError as e:
        print(f"RuntimeError: {e}")
    except Exception as e:
        print(f"Error: {e}")

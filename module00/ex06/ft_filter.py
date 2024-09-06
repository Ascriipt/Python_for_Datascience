def ft_filter(function, iterable):
    """_summary_

    Args:
        func (typing.Callable[..., any]): any function
        iterated (typing.Iterable[any]): any iterable object

    Returns:
        typing.Iterable[any]: any iterable object
    """
    return [x for x in iterable if function(x)]

import typing
"""
    importing 'typing'
"""


def ft_filter(func: typing.Callable[..., any],
              iterated: typing.Iterable[any]) -> typing.Iterable[any]:
    """_summary_

    Args:
        func (typing.Callable[..., any]): any function
        iterated (typing.Iterable[any]): any iterable object

    Returns:
        typing.Iterable[any]: any iterable object
    """
    return [x for x in iterated if func(x)]

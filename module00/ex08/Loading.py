import sys
import time
import shutil


def formatter(scd):
    """

    Args:
        scd (_type_): _description_

    Returns:
        _type_: _description_
    """
    minutes, seconds = divmod(scd, 60)
    return f"{int(minutes):02d}:{int(seconds):02d}"


def ft_tqdm(lst: range) -> None:
    """
    A simple progress bar function that simulates a tqdm-like progress bar in the terminal.
    Args:
        lst (range): A range object or any iterable to track progress over.
    """
    total = len(lst)
    start = time.time()

    for i, val in enumerate(lst, start=1):
        elapsed_time = time.time() - start
        speed = i / elapsed_time if elapsed_time > 0 else 0
        eta = (total - i) / speed if speed > 0 else 0

        elapsed_formatted = formatter(elapsed_time)
        eta_formatted = formatter(eta)

        progress_percentage = int(i / total * 100)
        left = f"{progress_percentage:3d}%|"
        right = f"| {i}/{total} [{elapsed_formatted}<{eta_formatted}, {speed:.2f}it/s]"

        blocks = [' ', '▏', '▎', '▍', '▌', '▋', '▊', '▉', '█']
        terminal_width = shutil.get_terminal_size((100, 20)).columns
        bar_width = terminal_width - len(left) - len(right)
        if bar_width < 1:
            bar_width = 1

        progress_exact = i / total * bar_width
        full_blocks = int(progress_exact)
        partial_block_idx = int((progress_exact - full_blocks) * 8)
        if full_blocks < bar_width:
            progress_bar = (
                '█' * full_blocks +
                blocks[partial_block_idx] +
                ' ' * (bar_width - full_blocks - 1)
            )
        else:
            progress_bar = '█' * bar_width

        sys.stdout.write('\r' + left + progress_bar + right)
        sys.stdout.flush()
        yield val
    print()

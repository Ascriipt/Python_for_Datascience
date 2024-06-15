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

    Args:
        lst (range): _description_

    Yields:
        _type_: _description_
    """
    total = len(lst)
    start = time.time()

    full_width = shutil.get_terminal_size().columns - 30
    tqdm_width = full_width - 10

    for i, val in enumerate(lst, start=1):
        progress = int(i / total * tqdm_width)
        elapsed_time = time.time() - start
        speed = i / elapsed_time
        eta = (total - i) / speed

        elapsed_formatted = formatter(elapsed_time)
        eta_formatted = formatter(eta)

        progress_bar = f"|{'█' * progress:<{tqdm_width}}|"
        progress_percentage = progress * 100 // tqdm_width
        progress_info = f"{progress_percentage}%{progress_bar} {i}/{total}"
        time_info = f"[{elapsed_formatted}<{eta_formatted}, {speed:.2f}it/s]"
        print(f"\r{progress_info} {time_info}", end="", flush=True)
        yield val

import datetime

now = datetime.datetime.now()
base = now - datetime.datetime(1970, 1, 1)


def format_time():
    print("Seconds since January 1, 1970: " f"{base.total_seconds():,.4f}"
          " or " f"{base.total_seconds():e}" " in scientific notation")
    print(f"Seconds since January 1, 1970: {base.total_seconds():,.4f} or {base.total_seconds():e} in scientific notation")
    print(now.strftime("%b %d %Y"))


format_time()

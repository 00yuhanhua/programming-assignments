import datetime as dt
import random as r


def random_time_generator() -> dt.time:
    hour: int = r.randint(8, 19)
    minu: int = r.randint(0, 59)
    sec: int = r.randint(0, 59)
    time: dt.time = dt.time(hour, minu, sec)
    return time

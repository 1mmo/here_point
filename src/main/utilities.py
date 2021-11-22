from datetime import datetime
from os.path import splitext


def get_timestamp_path(instance, filename) -> str:
    """ Change file name for image """
    return f'{datetime.now().timestamp()}{splitext(filename)[1])}'

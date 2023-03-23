from datetime import datetime


def get_time():
    current_time = datetime.now().time()
    return str(current_time)
